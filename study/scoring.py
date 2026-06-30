class ScoreTracker:
    def __init__(self):
        self.first_attempt_correct = 0
        self.first_attempt_missed = 0
        self.review_corrected = 0
        self.completed = 0
        self.missed_questions = []

    def record_answer(self, question, is_correct):
        self.completed += 1

        if is_correct:
            self.first_attempt_correct += 1
        else:
            self.first_attempt_missed += 1
            self.missed_questions.append(question)

    def record_review_answer(self, is_correct):
        if is_correct:
            self.review_corrected += 1

    def summary(self):
        return {
            "first_attempt_correct": self.first_attempt_correct,
            "first_attempt_missed": self.first_attempt_missed,
            "review_corrected": self.review_corrected,
            "completed": self.completed,
        }