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

class SynQuestion(Question):
    def __init__(self, question, choices, correct):
        self.question = question
        self.choices = choices
        self.correct = correct
        self.kind = "synonym"

class NotSynQuestion(Question):
    def __init__(choices, correct):
        self.choices = choices
        self.correct = correct
        self.kind = "synonym"

    def printQuestion(self):
        print("Which word is out of place in this group of words: ")
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


questions = [


NotSynQuestion(["support", "protest", "objection", "challenge"], "support"),
NotSynQuestion("annoy", ["pester", "anger", "please"], "please"),
NotSynQuestion("help", ["aid", "hinder", "assist"], "hinder"),
NotSynQuestion("attempt", ["desperate", "try", "endeavour"], "desperate"),
NotSynQuestion("wonder", ["awe", "courage", "amazement"], ""),
NotSynQuestion("sphere", ["globe", "orb", "hemisphere"], ""),
NotSynQuestion("diameter", ["width", "length", "breadth"], ""),
NotSynQuestion("assist", ["hamper", "hinder", "impede"], ""),
NotSynQuestion("alter", ["church", "change", "modify"], ""),
NotSynQuestion("rubbish", ["decline", "waste", "refuse"], ""),
NotSynQuestion("right", ["proper", "left", "just"], ""),
NotSynQuestion("ring", ["core", "chime", "peal"], ""),
NotSynQuestion("strike", ["hit", "beat", "mark"], ""),
NotSynQuestion("study", ["learn", "office", "bureau"], ""),
NotSynQuestion("tariff", ["duty", "tax", "deposit"], ""),
NotSynQuestion("ample", ["abundant", "plentiful", "scarce"], ""),
NotSynQuestion("tears", ["weep", "cry", "sob"], ""),
NotSynQuestion("taunt", ["tease", "jeer", "bluff"], ""),
NotSynQuestion("youthful", ["senior", "adolescent", "juvenile"], ""),
NotSynQuestion("hurried", ["abrupt", "linger", "hasty"], ""),
NotSynQuestion("edible", ["acrid", "bitter", "sour"], ""),
NotSynQuestion("accidental", ["mindfully", "involuntary", "inadvertent"], ""),
NotSynQuestion("enlarge", ["minute", "magnify", "augment"], ""),
NotSynQuestion("abandon", ["ceasefire", "leave", "advance"], ""),
NotSynQuestion("real", ["copy", "genuine", "actual"], "")

]

correct = 0
print(" ")
item = 0
q = questions[:20]
for question in q:
    item = item + 1
    print("\n\n")
    print(str(item) + " / " + str(len(q)))
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
print("not correct: ", len(q) - correct)
