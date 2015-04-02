import datetime
import random

from questions import Add, Multiply

class Quiz():
    questions = []
    answers = []
    def __init__(self):
        question_types = (Add, Multiply)
        for _ in range(10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1,10)
            question = random.choice(question_types)(num1, num2)
            self.questions.append(question)

    def take_quiz(self):
        self.start_time = datetime.datetime.now()

        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.end_time = datetime.datetime.now()

        return self.summary()

    def ask(self, question):
        correct = False
        question_start = datetime.datetime.now()
        answer = input(question.text + " = ")

        if answer == str(question.answer):
            correct = True

        question_end = datetime.datetime.now()
        return correct, question_end - question_start

    def total_correct(self):
        total = 0
        for answer in self.answers:
            if answer[0]:
                print(total)
                total += 1

        return total

    def summary(self):
        print("You got {} out of {} right.".format(self.total_correct(), len(self.questions)))
        print("It took you {} seconds.".format((self.end_time-self.start_time).seconds))

Quiz().take_quiz()