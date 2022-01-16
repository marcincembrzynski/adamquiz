import random

class Question:
    def __init__(self, question, choices, correct):
        self.question = question
        self.choices = choices
        self.correct = correct
        self.kind = "test"

    def isCorrect(self, value):
        return self.correct == value

    def printQuestion(self):
        print("enter " + self.kind + " for: " + self.question)
        print("---------------")
        for choice in self.choices:
            print(choice)
        print("---------------")


class AntQuestion(Question):
    def __init__(self, question, choices, correct):
        self.question = question
        self.choices = choices
        self.correct = correct
        self.kind = "antonym"
        
    def printQuestion(self):
        print("enter " + self.kind + " for: " + self.question)
        print("---------------")
        for choice in self.choices:
            print(choice)
        print("---------------")


class SynQuestion(Question):
    def __init__(self, question, choices, correct):
        self.question = question
        self.choices = choices
        self.correct = correct
        self.kind = "synonym"

class NotSynQuestion(Question):
    def __init__(self, choices, correct):
        self.choices = choices
        self.correct = correct
        self.kind = "synonym"

    def printQuestion(self):
        print("Which word is out of place in this group of words: ")
        print("---------------")
        for choice in self.choices:
            print(choice)
        print("---------------")





class Quiz:
    def __init__(self, questions):
        self.questions = questions


    def test(self):
        correct = 0
        print(" ")
        random.shuffle(self.questions)
        item = 0
        for question in self.questions:
            item = item + 1
            print("\n\n")
            print(str(item) + " / " + str(len(self.questions)))
            question.printQuestion()
            answer = raw_input("answer:")
            print(answer)
            if question.isCorrect(answer):
                print("---------------")
                for x in range(10):
                    print("ok!"* x)
                print("---------------")
                correct = correct + 1
            else:
                print("---------------")
                print("correct answer: ", question.correct)
                print("---------------")

            raw_input("press any key to continue....")

        print("correct: ", correct)
        print("not correct: ", len(self.questions) - correct)
