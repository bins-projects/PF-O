"""PrepFlow desktop application shell."""

from __future__ import annotations

from collections import OrderedDict
import random
import tkinter as tk
from tkinter import ttk

from study.loader import list_packs, load_pack
from study.question import check_answer, get_correct_answers, get_prompt
from study.review import ReviewQueue
from study.save_state import (
    delete_saved_session,
    has_saved_session,
    load_session,
    save_session,
)
from study.scoring import ScoreTracker
from study.session import SessionManager


DISPLAY_NAMES = {
    "Fundamentals of Nursing": "Fundamentals",
    "Pharmacy": "Pharmacy",
    "Medical-Surgical": "Medical-Surgical",
}

DISPLAY_ORDER = {
    "Fundamentals": 0,
    "Pharmacy": 1,
    "Medical-Surgical": 2,
}


class PrepFlowApp(tk.Tk):
    """Main PrepFlow desktop window."""

    def __init__(self) -> None:
        super().__init__()

        self.title("PrepFlow")
        self.geometry("1000x700")
        self.minsize(820, 580)

        self.current_frame: ttk.Frame | None = None
        self.chapter_variables: dict[tuple[object, str], tk.BooleanVar] = {}

        self._configure_styles()
        self.show_home_screen()

    def _configure_styles(self) -> None:
        style = ttk.Style(self)

        if "clam" in style.theme_names():
            style.theme_use("clam")

        style.configure(
            "Title.TLabel",
            font=("TkDefaultFont", 34, "bold"),
        )
        style.configure(
            "Subtitle.TLabel",
            font=("TkDefaultFont", 14),
        )
        style.configure(
            "Subject.TButton",
            font=("TkDefaultFont", 15, "bold"),
            padding=(16, 22),
        )
        style.configure(
            "Count.TLabel",
            font=("TkDefaultFont", 11),
        )
        style.configure(
            "Chapter.TCheckbutton",
            font=("TkDefaultFont", 12),
            padding=(8, 8),
        )
        style.configure(
            "Primary.TButton",
            font=("TkDefaultFont", 12, "bold"),
            padding=(18, 10),
        )

    def _replace_screen(self) -> ttk.Frame:
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = ttk.Frame(self, padding=32)
        self.current_frame.pack(fill="both", expand=True)
        return self.current_frame

    def show_home_screen(self) -> None:
        container = self._replace_screen()

        header = ttk.Frame(container)
        header.pack(fill="x", pady=(10, 38))

        ttk.Label(
            header,
            text="PrepFlow",
            style="Title.TLabel",
            anchor="center",
        ).pack(fill="x")

        ttk.Label(
            header,
            text="Choose a study category",
            style="Subtitle.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(10, 0))

        if has_saved_session():
            ttk.Button(
                container,
                text="Resume Saved Session",
                style="Primary.TButton",
                command=self._resume_saved_session,
            ).pack(pady=(0, 20))

        subjects = []
        for pack_info in list_packs():
            display_name = DISPLAY_NAMES.get(
                pack_info["title"],
                pack_info["title"],
            )
            subjects.append(
                {
                    "display_name": display_name,
                    "question_count": pack_info["question_count"],
                    "pack_info": pack_info,
                }
            )

        subjects.sort(
            key=lambda subject: DISPLAY_ORDER.get(
                subject["display_name"],
                99,
            )
        )

        cards = ttk.Frame(container)
        cards.pack(fill="both", expand=True)

        for column in range(3):
            cards.columnconfigure(column, weight=1, uniform="subjects")
        cards.rowconfigure(0, weight=1)

        for column, subject in enumerate(subjects):
            card = ttk.Frame(cards, padding=10)
            card.grid(
                row=0,
                column=column,
                padx=10,
                pady=10,
                sticky="nsew",
            )

            ttk.Button(
                card,
                text=subject["display_name"],
                style="Subject.TButton",
                command=lambda selected=subject: self.show_chapter_screen(
                    selected
                ),
            ).pack(fill="both", expand=True)

            ttk.Label(
                card,
                text=f'{subject["question_count"]:,} questions',
                style="Count.TLabel",
                anchor="center",
            ).pack(fill="x", pady=(12, 0))

        ttk.Label(
            container,
            text="Select a category to choose chapters and begin studying.",
            anchor="center",
        ).pack(fill="x", pady=(25, 5))

    def show_chapter_screen(self, subject: dict) -> None:
        container = self._replace_screen()
        pack = load_pack(subject["pack_info"]["path"])

        chapter_counts: OrderedDict[tuple[object, str], int] = OrderedDict()

        for question in pack["questions"]:
            chapter_number = question.get("chapter")
            chapter_title = question.get("chapter_title") or "Untitled Chapter"
            key = (chapter_number, chapter_title)
            chapter_counts[key] = chapter_counts.get(key, 0) + 1

        self.chapter_variables = {
            key: tk.BooleanVar(value=False)
            for key in chapter_counts
        }

        top_bar = ttk.Frame(container)
        top_bar.pack(fill="x")

        ttk.Button(
            top_bar,
            text="← Back",
            command=self.show_home_screen,
        ).pack(side="left")

        ttk.Label(
            top_bar,
            text=subject["display_name"],
            style="Title.TLabel",
            anchor="center",
        ).pack(side="left", expand=True)

        ttk.Label(
            top_bar,
            text=f'{subject["question_count"]:,} questions',
            style="Count.TLabel",
        ).pack(side="right")

        ttk.Label(
            container,
            text="Choose one or more chapters",
            style="Subtitle.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(14, 18))

        controls = ttk.Frame(container)
        controls.pack(fill="x", pady=(0, 12))

        ttk.Button(
            controls,
            text="Select All",
            command=self._select_all_chapters,
        ).pack(side="left")

        ttk.Button(
            controls,
            text="Clear All",
            command=self._clear_all_chapters,
        ).pack(side="left", padx=(8, 0))

        self.selection_label = ttk.Label(
            controls,
            text="0 chapters selected",
        )
        self.selection_label.pack(side="right")

        list_container = ttk.Frame(container)
        list_container.pack(fill="both", expand=True)

        canvas = tk.Canvas(
            list_container,
            highlightthickness=0,
            borderwidth=0,
        )
        scrollbar = ttk.Scrollbar(
            list_container,
            orient="vertical",
            command=canvas.yview,
        )
        chapter_frame = ttk.Frame(canvas)

        chapter_frame.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion=canvas.bbox("all")
            ),
        )

        canvas_window = canvas.create_window(
            (0, 0),
            window=chapter_frame,
            anchor="nw",
        )

        canvas.bind(
            "<Configure>",
            lambda event: canvas.itemconfigure(
                canvas_window,
                width=event.width,
            ),
        )

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for row, ((chapter_number, chapter_title), count) in enumerate(
            chapter_counts.items()
        ):
            if chapter_number is None:
                label = chapter_title
            else:
                label = f"Chapter {chapter_number}: {chapter_title}"

            label = f"{label}  —  {count:,} questions"

            ttk.Checkbutton(
                chapter_frame,
                text=label,
                variable=self.chapter_variables[
                    (chapter_number, chapter_title)
                ],
                style="Chapter.TCheckbutton",
                command=self._update_selection_status,
            ).grid(
                row=row,
                column=0,
                sticky="w",
                padx=10,
                pady=2,
            )

        bottom_bar = ttk.Frame(container)
        bottom_bar.pack(fill="x", pady=(18, 0))

        self.start_button = ttk.Button(
            bottom_bar,
            text="Start Studying",
            style="Primary.TButton",
            state="disabled",
            command=lambda: self._start_studying(subject, pack),
        )
        self.start_button.pack(side="right")

    def _select_all_chapters(self) -> None:
        for variable in self.chapter_variables.values():
            variable.set(True)
        self._update_selection_status()

    def _clear_all_chapters(self) -> None:
        for variable in self.chapter_variables.values():
            variable.set(False)
        self._update_selection_status()

    def _update_selection_status(self) -> None:
        selected_count = sum(
            variable.get()
            for variable in self.chapter_variables.values()
        )

        word = "chapter" if selected_count == 1 else "chapters"
        self.selection_label.configure(
            text=f"{selected_count} {word} selected"
        )

        self.start_button.configure(
            state="normal" if selected_count else "disabled"
        )

    def _start_studying(self, subject: dict, pack: dict) -> None:
        selected_chapters = {
            key
            for key, variable in self.chapter_variables.items()
            if variable.get()
        }

        selected_questions = [
            question
            for question in pack["questions"]
            if (
                question.get("chapter"),
                question.get("chapter_title") or "Untitled Chapter",
            )
            in selected_chapters
        ]

        supported_types = {
            "mc",
            "multiple_choice",
            "multiple_response",
            "completion",
            "ordering",
            "ordered_response",
        }

        supported_questions = [
            question
            for question in selected_questions
            if question.get("type") in supported_types
        ]

        if not supported_questions:
            self._show_message_screen(
                title="No Questions Available",
                message=(
                    "No supported study questions were found in the "
                    "selected chapters."
                ),
                button_text="Back to Chapters",
                command=lambda: self.show_chapter_screen(subject),
            )
            return

        self.session_subject = subject
        self.session_pack_path = str(subject["pack_info"]["path"])
        self.session = SessionManager(
            supported_questions,
            block_size=15,
        )
        self.score = ScoreTracker()
        self.review = ReviewQueue()

        self.review_mode = False
        self.current_question = None
        self.answer_submitted = False

        self.block_correct = 0
        self.block_missed = 0

        self._load_next_first_attempt_question()

    def _current_block_size(self) -> int:
        total_questions = self.session.total_questions()
        block_size = self.session.block_size
        block_number = self.session.current_block_number()

        block_start = (block_number - 1) * block_size
        remaining = total_questions - block_start

        return min(block_size, remaining)

    def _load_next_first_attempt_question(self) -> None:
        if not self.session.has_next_question():
            self._show_session_complete()
            return

        self.review_mode = False
        self.current_question = self.session.get_next_question()
        self.answer_submitted = False
        self._show_question_screen()

    def _show_question_screen(self) -> None:
        question = self.current_question
        self._save_current_session()
        container = self._replace_screen()

        top_bar = ttk.Frame(container)
        top_bar.pack(fill="x")

        ttk.Button(
            top_bar,
            text="← Exit Session",
            command=self.show_home_screen,
        ).pack(side="left")

        ttk.Label(
            top_bar,
            text=self.session_subject["display_name"],
            style="Subtitle.TLabel",
        ).pack(side="left", expand=True)

        if self.review_mode:
            position_text = (
                f"Mastery Review • {self.review.count() + 1} remaining"
            )
        else:
            position_text = (
                f"Block {self.session.current_block_number()} • "
                f"Question {self.session.question_in_block()} "
                f"of {self._current_block_size()}"
            )

        ttk.Label(
            top_bar,
            text=position_text,
        ).pack(side="right")

        progress = ttk.Progressbar(
            container,
            maximum=self.session.total_questions(),
            value=self.session.completed_questions(),
        )
        progress.pack(fill="x", pady=(18, 12))

        # Keep navigation controls visible regardless of question length.
        bottom_bar = ttk.Frame(container)
        bottom_bar.pack(side="bottom", fill="x", pady=(12, 0))

        summary = self.score.summary()

        ttk.Label(
            bottom_bar,
            text=(
                f'First pass: {summary["first_attempt_correct"]} correct, '
                f'{summary["first_attempt_missed"]} missed'
            ),
        ).pack(side="left")

        self.submit_button = ttk.Button(
            bottom_bar,
            text="Submit Answer",
            style="Primary.TButton",
            state="disabled",
            command=self._submit_current_answer,
        )
        self.submit_button.pack(side="right")

        self.next_button = ttk.Button(
            bottom_bar,
            text="Continue",
            style="Primary.TButton",
            command=self._advance_after_answer,
        )

        # The question, choices, feedback, and rationale scroll together.
        content_container = ttk.Frame(container)
        content_container.pack(fill="both", expand=True)

        canvas = tk.Canvas(
            content_container,
            highlightthickness=0,
            borderwidth=0,
        )
        scrollbar = ttk.Scrollbar(
            content_container,
            orient="vertical",
            command=canvas.yview,
        )
        content = ttk.Frame(canvas, padding=(2, 10, 12, 18))

        content.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion=canvas.bbox("all")
            ),
        )

        canvas_window = canvas.create_window(
            (0, 0),
            window=content,
            anchor="nw",
        )

        canvas.bind(
            "<Configure>",
            lambda event: canvas.itemconfigure(
                canvas_window,
                width=event.width,
            ),
        )

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        ttk.Label(
            content,
            text=get_prompt(question),
            font=("TkDefaultFont", 15),
            wraplength=820,
            justify="left",
        ).pack(fill="x", anchor="w", pady=(0, 20))

        question_type = self._normalized_question_type(question)

        choices_frame = ttk.Frame(content)
        choices_frame.pack(fill="x")

        if question_type == "multiple_choice":
            self.selected_answer = tk.StringVar(value="")

            for choice in question.get("choices", []):
                ttk.Radiobutton(
                    choices_frame,
                    text=f'{choice["label"]}. {choice["text"]}',
                    variable=self.selected_answer,
                    value=choice["label"],
                    command=self._update_submit_state,
                ).pack(
                    fill="x",
                    anchor="w",
                    padx=10,
                    pady=8,
                )

        elif question_type == "multiple_response":
            self.response_variables = {}

            ttk.Label(
                choices_frame,
                text="Select all that apply.",
                font=("TkDefaultFont", 11, "italic"),
            ).pack(fill="x", anchor="w", padx=10, pady=(0, 6))

            for choice in question.get("choices", []):
                variable = tk.BooleanVar(value=False)
                self.response_variables[choice["label"]] = variable

                ttk.Checkbutton(
                    choices_frame,
                    text=f'{choice["label"]}. {choice["text"]}',
                    variable=variable,
                    command=self._update_submit_state,
                ).pack(
                    fill="x",
                    anchor="w",
                    padx=10,
                    pady=8,
                )

        elif question_type == "completion":
            self.completion_answer = tk.StringVar(value="")

            ttk.Label(
                choices_frame,
                text="Enter your answer:",
                font=("TkDefaultFont", 11, "bold"),
            ).pack(fill="x", anchor="w", padx=10, pady=(0, 6))

            completion_entry = ttk.Entry(
                choices_frame,
                textvariable=self.completion_answer,
                font=("TkDefaultFont", 13),
            )
            completion_entry.pack(fill="x", padx=10, pady=8)
            completion_entry.bind(
                "<KeyRelease>",
                lambda event: self._update_submit_state(),
            )
            completion_entry.focus_set()

        elif question_type == "ordered_response":
            self.ordered_choices = list(question.get("choices", []))

            ttk.Label(
                choices_frame,
                text=(
                    "Click and hold an item, then drag it into the "
                    "correct position."
                ),
                font=("TkDefaultFont", 11, "italic"),
                wraplength=800,
                justify="left",
            ).pack(fill="x", anchor="w", padx=10, pady=(0, 8))

            ordering_area = ttk.Frame(choices_frame)
            ordering_area.pack(fill="x", padx=10)

            self.ordering_listbox = tk.Listbox(
                ordering_area,
                height=max(4, len(self.ordered_choices)),
                font=("TkDefaultFont", 12),
                selectmode="browse",
                exportselection=False,
            )
            self.ordering_listbox.pack(
                fill="both",
                expand=True,
            )

            self._dragged_order_index = None

            self.ordering_listbox.bind(
                "<Button-1>",
                self._start_order_drag,
            )
            self.ordering_listbox.bind(
                "<B1-Motion>",
                self._drag_ordered_choice,
            )
            self.ordering_listbox.bind(
                "<ButtonRelease-1>",
                self._finish_order_drag,
            )

            self._refresh_ordering_listbox()

        self.feedback_frame = ttk.Frame(content)
        self.feedback_frame.pack(fill="x", pady=(20, 0))

    @staticmethod
    def _normalized_question_type(question: dict) -> str:
        question_type = question.get("type")

        if question_type in {"mc", "multiple_choice"}:
            return "multiple_choice"

        if question_type in {"ordering", "ordered_response"}:
            return "ordered_response"

        return question_type

    def _current_user_answer(self) -> str:
        question_type = self._normalized_question_type(
            self.current_question
        )

        if question_type == "multiple_choice":
            return self.selected_answer.get()

        if question_type == "multiple_response":
            return "".join(
                label
                for label, variable in self.response_variables.items()
                if variable.get()
            )

        if question_type == "completion":
            return self.completion_answer.get().strip()

        if question_type == "ordered_response":
            return "".join(
                choice["label"]
                for choice in self.ordered_choices
            )

        return ""

    def _update_submit_state(self) -> None:
        if self.answer_submitted:
            return

        question_type = self._normalized_question_type(
            self.current_question
        )

        if question_type == "ordered_response":
            has_answer = bool(self.ordered_choices)
        else:
            has_answer = bool(self._current_user_answer())

        self.submit_button.configure(
            state="normal" if has_answer else "disabled"
        )

    def _start_order_drag(self, event) -> None:
        index = self.ordering_listbox.nearest(event.y)

        if 0 <= index < len(self.ordered_choices):
            self._dragged_order_index = index
            self.ordering_listbox.selection_clear(0, tk.END)
            self.ordering_listbox.selection_set(index)
            self.ordering_listbox.activate(index)

    def _drag_ordered_choice(self, event) -> None:
        if self._dragged_order_index is None:
            return

        target_index = self.ordering_listbox.nearest(event.y)
        target_index = max(
            0,
            min(target_index, len(self.ordered_choices) - 1),
        )

        if target_index == self._dragged_order_index:
            return

        choice = self.ordered_choices.pop(self._dragged_order_index)
        self.ordered_choices.insert(target_index, choice)
        self._dragged_order_index = target_index

        self._refresh_ordering_listbox()
        self.ordering_listbox.selection_set(target_index)
        self.ordering_listbox.activate(target_index)
        self.ordering_listbox.see(target_index)

    def _finish_order_drag(self, event) -> None:
        if self._dragged_order_index is not None:
            self.ordering_listbox.selection_clear(0, tk.END)
            self.ordering_listbox.selection_set(
                self._dragged_order_index
            )

        self._dragged_order_index = None

    def _refresh_ordering_listbox(self) -> None:
        self.ordering_listbox.delete(0, tk.END)

        for choice in self.ordered_choices:
            self.ordering_listbox.insert(
                tk.END,
                f'{choice["label"]}. {choice["text"]}',
            )

        self._update_submit_state()

    def _move_ordered_choice(self, direction: int) -> None:
        selection = self.ordering_listbox.curselection()

        if not selection:
            return

        current_index = selection[0]
        new_index = current_index + direction

        if new_index < 0 or new_index >= len(self.ordered_choices):
            return

        self.ordered_choices[current_index], self.ordered_choices[new_index] = (
            self.ordered_choices[new_index],
            self.ordered_choices[current_index],
        )

        self._refresh_ordering_listbox()
        self.ordering_listbox.selection_set(new_index)
        self.ordering_listbox.activate(new_index)
        self.ordering_listbox.see(new_index)

    def _submit_current_answer(self) -> None:
        if self.answer_submitted:
            return

        question = self.current_question
        correct_answers = get_correct_answers(question)

        question_type = self._normalized_question_type(question)

        is_correct = check_answer(
            self._current_user_answer(),
            correct_answers,
            question_type,
        )

        self.answer_submitted = True
        self.submit_button.configure(state="disabled")

        if self.review_mode:
            self.score.record_review_answer(is_correct)

            if not is_correct:
                self.review.add(question)
        else:
            self.score.record_answer(question, is_correct)

            if is_correct:
                self.block_correct += 1
            else:
                self.block_missed += 1
                self.review.add(question)

        if is_correct:
            feedback_text = "Correct!"
        else:
            correct_text = ", ".join(correct_answers)
            feedback_text = f"Incorrect. Correct answer: {correct_text}"

        ttk.Label(
            self.feedback_frame,
            text=feedback_text,
            font=("TkDefaultFont", 13, "bold"),
            wraplength=850,
            justify="left",
        ).pack(fill="x", anchor="w", pady=(0, 12))

        ttk.Label(
            self.feedback_frame,
            text="Rationale",
            font=("TkDefaultFont", 12, "bold"),
        ).pack(fill="x", anchor="w")

        ttk.Label(
            self.feedback_frame,
            text=question.get("rationale", ""),
            wraplength=850,
            justify="left",
        ).pack(fill="x", anchor="w", pady=(6, 0))

        self.next_button.pack(side="right")
        self.submit_button.pack_forget()

    def _advance_after_answer(self) -> None:
        if self.review_mode:
            if self.review.has_questions():
                self.current_question = self.review.next_question()
                self.answer_submitted = False
                self._show_question_screen()
            else:
                self._show_review_complete()
            return

        block_finished = self.session.is_block_complete()
        session_finished = not self.session.has_next_question()

        if block_finished or session_finished:
            self._show_block_complete()
        else:
            self._load_next_first_attempt_question()

    def _show_block_complete(self) -> None:
        container = self._replace_screen()
        block_number = self.session.current_block_number()

        ttk.Label(
            container,
            text=f"Block {block_number} Complete",
            style="Title.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(70, 18))

        total = self.block_correct + self.block_missed

        ttk.Label(
            container,
            text=(
                f"First-pass score: {self.block_correct} of {total}\n"
                f"Missed questions to review: {self.review.count()}"
            ),
            style="Subtitle.TLabel",
            anchor="center",
            justify="center",
        ).pack(fill="x", pady=(0, 30))

        if self.review.has_questions():
            ttk.Button(
                container,
                text="Review Missed Questions",
                style="Primary.TButton",
                command=self._begin_review,
            ).pack()
        elif self.session.has_next_question():
            ttk.Button(
                container,
                text="Begin Next Block",
                style="Primary.TButton",
                command=self._begin_next_block,
            ).pack()
        else:
            ttk.Button(
                container,
                text="View Session Results",
                style="Primary.TButton",
                command=self._show_session_complete,
            ).pack()

    def _begin_review(self) -> None:
        self.review_mode = True
        self.current_question = self.review.next_question()
        self.answer_submitted = False
        self._show_question_screen()

    def _show_review_complete(self) -> None:
        container = self._replace_screen()

        ttk.Label(
            container,
            text="Review Complete",
            style="Title.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(80, 18))

        ttk.Label(
            container,
            text="All missed questions from this block are now mastered.",
            style="Subtitle.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(0, 30))

        if self.session.has_next_question():
            ttk.Button(
                container,
                text="Begin Next Block",
                style="Primary.TButton",
                command=self._begin_next_block,
            ).pack()
        else:
            ttk.Button(
                container,
                text="View Session Results",
                style="Primary.TButton",
                command=self._show_session_complete,
            ).pack()

    def _begin_next_block(self) -> None:
        self.block_correct = 0
        self.block_missed = 0
        self.review_mode = False
        self._load_next_first_attempt_question()

    def _save_current_session(self) -> None:
        if self.current_question is None:
            return

        summary = self.score.summary()

        save_session(
            {
                "pack_path": self.session_pack_path,
                "subject_display_name": self.session_subject["display_name"],
                "subject_question_count": self.session_subject[
                    "question_count"
                ],
                "question_order": [
                    question["id"]
                    for question in self.session.questions
                ],
                "current_index": self.session.current_index,
                "current_question_id": self.current_question["id"],
                "block_size": self.session.block_size,
                "review_mode": self.review_mode,
                "review_question_ids": [
                    question["id"]
                    for question in self.review.questions
                ],
                "score": summary,
                "missed_question_ids": [
                    question["id"]
                    for question in self.score.missed_questions
                ],
                "block_correct": self.block_correct,
                "block_missed": self.block_missed,
            }
        )

    def _resume_saved_session(self) -> None:
        state = load_session()

        if state is None:
            self.show_home_screen()
            return

        try:
            pack = load_pack(state["pack_path"])
            questions_by_id = {
                question["id"]: question
                for question in pack["questions"]
            }

            ordered_questions = [
                questions_by_id[question_id]
                for question_id in state["question_order"]
            ]

            current_question = questions_by_id[
                state["current_question_id"]
            ]

            review_questions = [
                questions_by_id[question_id]
                for question_id in state.get(
                    "review_question_ids",
                    [],
                )
            ]

            missed_questions = [
                questions_by_id[question_id]
                for question_id in state.get(
                    "missed_question_ids",
                    [],
                )
            ]
        except (KeyError, TypeError, ValueError):
            delete_saved_session()
            self.show_home_screen()
            return

        self.session_subject = {
            "display_name": state["subject_display_name"],
            "question_count": state["subject_question_count"],
            "pack_info": {
                "path": state["pack_path"],
            },
        }
        self.session_pack_path = state["pack_path"]

        self.session = SessionManager(
            ordered_questions,
            block_size=state.get("block_size", 15),
        )
        self.session.questions = ordered_questions
        self.session.current_index = state["current_index"]

        self.review = ReviewQueue()
        self.review.questions = review_questions

        self.score = ScoreTracker()
        score_state = state.get("score", {})
        self.score.first_attempt_correct = score_state.get(
            "first_attempt_correct",
            0,
        )
        self.score.first_attempt_missed = score_state.get(
            "first_attempt_missed",
            0,
        )
        self.score.review_corrected = score_state.get(
            "review_corrected",
            0,
        )
        self.score.completed = score_state.get("completed", 0)
        self.score.missed_questions = missed_questions

        self.review_mode = state.get("review_mode", False)
        self.current_question = current_question
        self.answer_submitted = False
        self.block_correct = state.get("block_correct", 0)
        self.block_missed = state.get("block_missed", 0)

        self._show_question_screen()

    def _show_session_complete(self) -> None:
        delete_saved_session()
        container = self._replace_screen()
        summary = self.score.summary()

        total = summary["completed"]
        correct = summary["first_attempt_correct"]
        missed = summary["first_attempt_missed"]

        percentage = round((correct / total) * 100) if total else 0

        ttk.Label(
            container,
            text="Session Complete",
            style="Title.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(70, 18))

        ttk.Label(
            container,
            text=(
                f"First-pass score: {correct} of {total} ({percentage}%)\n"
                f"First-pass missed: {missed}\n"
                f"Review answers corrected: "
                f'{summary["review_corrected"]}\n\n'
                "Mastery complete"
            ),
            style="Subtitle.TLabel",
            anchor="center",
            justify="center",
        ).pack(fill="x", pady=(0, 30))

        ttk.Button(
            container,
            text="Return Home",
            style="Primary.TButton",
            command=self.show_home_screen,
        ).pack()

    def _show_message_screen(
        self,
        title: str,
        message: str,
        button_text: str,
        command,
    ) -> None:
        container = self._replace_screen()

        ttk.Label(
            container,
            text=title,
            style="Title.TLabel",
            anchor="center",
        ).pack(fill="x", pady=(80, 18))

        ttk.Label(
            container,
            text=message,
            style="Subtitle.TLabel",
            anchor="center",
            wraplength=700,
        ).pack(fill="x", pady=(0, 30))

        ttk.Button(
            container,
            text=button_text,
            style="Primary.TButton",
            command=command,
        ).pack()


def main() -> None:
    app = PrepFlowApp()
    app.mainloop()


if __name__ == "__main__":
    main()
