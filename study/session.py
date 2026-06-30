import random
class SessionManager:
    def __init__(self, questions, block_size=15):
        self.questions = questions.copy()
        random.shuffle(self.questions)
        self.current_index = 0
        self.block_size = block_size

    def has_next_question(self):
        return self.current_index < len(self.questions)

    def get_next_question(self):
        if not self.has_next_question():
            return None

        question = self.questions[self.current_index]
        self.current_index += 1
        return question

    def total_questions(self):
        return len(self.questions)

    def completed_questions(self):
        return self.current_index
    
    def current_block_number(self):
        if self.current_index == 0:
            return 1
        
        

        return ((self.current_index - 1) // self.block_size) + 1
    
    def question_in_block(self):
        return ((self.current_index - 1) % self.block_size) + 1

    def is_block_complete(self):
        return self.completed_questions() % self.block_size == 0