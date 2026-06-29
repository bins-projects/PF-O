class ReviewQueue:
    def __init__(self):
        self.questions = []

    def add(self, question):
        self.questions.append(question)

    def has_questions(self):
        return len(self.questions) > 0

    def next_question(self):
        if not self.has_questions():
            return None

        return self.questions.pop(0)

    def count(self):
        return len(self.questions)