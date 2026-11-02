from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer

    @abstractmethod
    def evaluate_answer(self, user_answer):
        pass

class MCQQuestion(Question):
    def evaluate_answer(self, user_answer):
        return user_answer.strip().upper() == self.correct_answer.strip().upper()

class TrueFalseQuestion(Question):
    def evaluate_answer(self, user_answer):
        return str(user_answer).strip().lower() == str(self.correct_answer).strip().lower()

class DescriptiveQuestion(Question):
    def evaluate_answer(self, user_answer):
        keywords = self.correct_answer
        return all(k.lower() in user_answer.lower() for k in keywords)

q1 = MCQQuestion('Capital of France? A) Berlin B) Paris', 'B')
q2 = TrueFalseQuestion('Python is statically typed? True/False', 'False')
q3 = DescriptiveQuestion('Define encapsulation', ['bundling', 'data', 'methods'])

print('Q1 Correct:', q1.evaluate_answer('B'))
print('Q2 Correct:', q2.evaluate_answer('false'))
print('Q3 Correct:', q3.evaluate_answer('Encapsulation is bundling data and methods together.'))
