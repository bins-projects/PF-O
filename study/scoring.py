class ScoreTracker:
    def __init__(self):
        self.correct = 0
        self.missed = 0
        self.completed = 0
        self.missed_questions = []

    def record_answer(self, question, is_correct):
        self.completed += 1

        if is_correct:
            self.correct += 1
        else:
            self.missed += 1
            self.missed_questions.append(question)

    def summary(self):
        return {
            "correct": self.correct,
            "missed": self.missed,
            "completed": self.completed,
        }