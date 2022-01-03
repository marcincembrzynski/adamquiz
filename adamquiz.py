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


class AntQuestion(Question):
    def __init__(self, question, choices, correct):
        self.question = question
        self.choices = choices
        self.correct = correct
        self.kind = "antonym"


questions = [
SynQuestion("drowsy" , ["awake", "cross", "sleepy", "active"], "sleepy"),
SynQuestion("depart", ["arrive", "decide", "slice", "leave"], "leave"),
SynQuestion("peril", ["safety", "extreme", "security", "danger"], "danger"),
SynQuestion("plucky", ["brave", "clever", "safety", "crazy"], "brave"),
SynQuestion("assist", ["hinder", "help", "manage", "cheat"], "help"),
SynQuestion("interior", ["design", "interest", "inside", "increase"], "inside"),
SynQuestion("end", ["depart", "gallop", "stop", "arrive"], "stop"),
SynQuestion("hasten", ["wait", "hurry", "leave", "tie"], "hurry"),
SynQuestion("descend", ["part", "go down", "go up", "spread"], "go down"),
SynQuestion("commence", ["begin", "stop", "business", "allowance"], "begin"),
SynQuestion("bold", ["dim", "hairless", "timid", "brave"], "hairless"),
SynQuestion("comprehend", ["manage", "understand", "realise", "listen"], "understand"),
SynQuestion("deteriorate", ["improve", "worsen", "detach", "damage"], "worsen"),
SynQuestion("many", ["multiply", "receive", "single", "numerous"], "numerous"),
SynQuestion("contemporary", ["former", "current", "traditional", "old"], "current"),

SynQuestion("dear", ["generous", "mean", "expensive", ""], "expensive"),
SynQuestion("buy", ["take", "give", "purchase", ""], "purchase"),
SynQuestion("give", ["borrow", "donate", "lend", ""], "donate"),
SynQuestion("pale", ["light", "dear", "cheap", ""], "light"),
SynQuestion("mediocre", ["massive", "slight", "slender", ""], "slight"),
SynQuestion("shiny", ["mild", "dim", "bright", ""], "bright"),
SynQuestion("depart", ["stay", "come", "go", ""], "go"),
SynQuestion("sour", ["salty", "sharp", "smooth", ""], "sharp"),
SynQuestion("concise", ["long", "case", "brief", ""], "brief"),
SynQuestion("informal", ["casual", "punctual", "late", ""], "casual"),
SynQuestion("occurence", ["immediate", "manage", "instance", ""], "instance"),
SynQuestion("liberty", ["freedom", "pass", "aloud", ""], "freedom"),
SynQuestion("enlarge", ["glass", "decrease", "magnify", ""], "magnify"),
SynQuestion("neccessary", ["request", "denied", "required", ""], "required"),
SynQuestion("proof", ["court", "evidence", "guilty", ""], "evidence"),
SynQuestion("inspect", ["examine", "lesson", "test", ""], "examine"),
SynQuestion("dive", ["plunge", "swim", "stroke", ""], "plunge"),
SynQuestion("significant", ["bizzare", "meaningful", "cleaver", ""], "meaningful"),
SynQuestion("proceed", ["continue", "retreat", "arrive", ""], "continue"),
SynQuestion("essential", ["needless", "random", "imperative", ""], "imperative"),

SynQuestion("high", ["leap", "loop", "lean", "lofty"], "lofty"),
SynQuestion("moisture", ["mellow", "dampness", "liquid", "most"], "dampness"),
SynQuestion("least", ["maximum", "mininum", "linger", "leisure"], "minimum"),
SynQuestion("dumb", ["bell", "mute", "pacify", "wild"], "mute"),
SynQuestion("disease", ["dealer", "health", "manage", "malady"], "malady"),
SynQuestion("fable", ["myth", "fail", "quote", "increase"], "myth"),
SynQuestion("most", ["damp", "maximum", "least", "average"], "maximum"),
SynQuestion("agile", ["agent", "decide", "nimble", "neccessary"], "nimble"),
SynQuestion("edge", ["under", "margin", "tense", "out"], "margin"),
SynQuestion("groan", ["grow", "group", "mow", "moan"], "moan"),
SynQuestion("rowdy", ["annoy", "noisy", "timid", "brave"], "noisy"),
SynQuestion("new", ["clean", "traditional", "modern", "frequent"], "modern"),
SynQuestion("choice", ["delegate", "compulsory", "option", "average"], "option"),
SynQuestion("peculiar", ["pretty", "amazing", "strange", "normal"], "strange"),
SynQuestion("plume", ["stone", "frequent", "feather", "placid"], "feather"),

SynQuestion("deluge", ["destroy", "flood", "scatter", "scold"], "flood"),
SynQuestion("detest", ["hate", "leave", "bread", "heave"], "hate"),
SynQuestion("forbidden", ["allowed", "prohibited", "forever", "ignore"], "prohibited"),
SynQuestion("deliberately", ["purposely", "definitely", "sparingly", "fully"], "purposely"),
SynQuestion("rectify", ["release", "maintain", "decide", "correct"], "correct"),
SynQuestion("rigid", ["subtle", "flexible", "stiff", "right"], "stiff"),
SynQuestion("strenous", ["straight", "vigorous", "easy", "light"], "vigorous"),
SynQuestion("sceptical", ["serious", "believing", "worrying", "unbeliewing"], "unbeliewing"),
SynQuestion("reside", ["live", "across", "opposite", "resident"], "live"),
SynQuestion("resist", ["withstand", "without", "withdraw", "wither"], "withstand"),
SynQuestion("submissive", ["obedient", "obnoxious", "obstinate", "obstruct"], "obedient"),
SynQuestion("profound", ["proof", "deep", "discover", "width"], "deep"),
SynQuestion("prudent", ["sorry", "perfect", "worry", "wise"], "wise"),
SynQuestion("interrogate", ["question", "intact", "elevate", "medidate"], "question"),
SynQuestion("mature", ["young", "ripe", "lessen", "control"], "ripe"),
SynQuestion("construct", ["allow", "build", "debate", "demolish"], "build"),
SynQuestion("persuade", ["convince", "pressure", "agree", "allow"], "convince"),
SynQuestion("recall", ["telephone", "retain", "remember", "shout"], "remember"),
SynQuestion("weary", ["weird", "clothes", "tired", "excited"], "tired"),
SynQuestion("dilligent", ["silly", "lazy", "slow", "hardworking"], "hardworking"),
SynQuestion("assault", ["attack", "condiment", "embrace", "flee"], "attack"),
SynQuestion("tepid", ["treatment", "scary", "tired", "lukewarm"], "lukewarm"),
SynQuestion("ponder", ["consider", "worry", "talk", "boast"], "consider"),
SynQuestion("remain", ["leave", "stay", "depart", "part"], "stay"),
SynQuestion("disperse", ["scatter", "combine", "displease", "gather"], "scatter"),
SynQuestion("odour", ["order", "ordeal", "smell", "small"], "smell"),
SynQuestion("abrupt", ["slowly", "kind", "abroad", "sudden"], "sudden"),
SynQuestion("brief", ["build", "understand", "short", "long"], "short"),
SynQuestion("reluctant", ["willing", "unwilling", "distrust", "lucky"], "unwilling"),
SynQuestion("loathe", ["love", "like", "hate", "keen"], "hate"),
SynQuestion("robust", ["weak", "strong", "lean", "lively"], "strong"),
SynQuestion("site", ["mellow", "vintage", "scene", "score"], "scene"),
SynQuestion("shrine", ["tomb", "shrink", "boat", "grave"], "tomb"),
SynQuestion("sleek", ["smooth", "weak", "snooze", "rough"], "smooth"),
SynQuestion("slender", ["dealer", "slim", "bend", "shake"], "slim"),
SynQuestion("squirm", ["shrink", "wail", "screech", "wriggle"], "wriggle"),
SynQuestion("steed", ["deer", "horse", "goat", "pig"], "horse"),
SynQuestion("stern", ["lenient", "storm", "strict", "chimmey"], "strict"),
SynQuestion("stubborn", ["obstinate", "control", "tense", "infant"], "obstinate"),
SynQuestion("sturdy", ["flexible", "stuck", "strong", "weak"], "strong"),
SynQuestion("surrender", ["yield", "give back", "frugal", "advance"], "yield"),
SynQuestion("suspend", ["accept", "hang", "convert", "frequent"], "hang"),
SynQuestion("terror", ["anxious", "dog", "option", "fear"], "fear"),
SynQuestion("tested", ["exam", "tried", "strange", "normal"], "tried"),
SynQuestion("thrust", ["leap", "tense", "pushed", "placid"], "pushed"),

AntQuestion("artificial", ["allow", "genuine", "debate", "demolish"], "genuine"),
AntQuestion("plural", ["convince", "detract", "singular", "allow"], "singular"),
AntQuestion("poverty", ["wealth", "retain", "remember", "present"], "wealth"),
AntQuestion("compulsory", ["weird", "voluntary", "tired", "excited"], "voluntary"),
AntQuestion("diligent", ["silly", "lazy", "slow", "hardworking"], "lazy"),
AntQuestion("permanent", ["attack", "condiment", "temporary", "flee"], "temporary"),
AntQuestion("reward", ["treatment", "discipline", "tired", "punishment"], "punishment"),
AntQuestion("deny", ["condider", "worry", "admit", "boast"], "admit"),
AntQuestion("severe", ["leave", "stay", "depart", "mild"], "mild"),
AntQuestion("conceal", ["combine", "displease", "gather", "reveal"], "reveal"),
AntQuestion("tranquil", ["order", "ordeal", "smell", "rough"], "rought"),
AntQuestion("barren", ["fertile", "kind", "abroad", "sudden"], "fertile"),
AntQuestion("permit", ["build", "understand", "forbid", "long"], "forbid"),
AntQuestion("foolish", ["willing", "unwilling", "resistant", "wise"], "wise"),
AntQuestion("frightened", ["scarce", "calm", "retreat", "leave"], "calm"),
AntQuestion("transparent", ["opaque", "clear", "genuine", "bright"], "opaque"),
AntQuestion("plain", ["fancy", "easy", "simple", "hard"], "fancy"),
AntQuestion("pedestrian", ["climber", "walker", "pilot", "motorist"], "motorist"),
AntQuestion("hero", ["coward", "simple", "adult", "infant"], "coward"),
AntQuestion("giant", ["glad", "massive", "dwarf", "jolly"], "dwarf"),
AntQuestion("unknown", ["fancy", "condiment", "well", "famous"], "famous"),
AntQuestion("smile", ["grin", "frown", "mouth", "pout"], "frown"),
AntQuestion("generous", ["consider", "mean", "kind", "boast"], "mean"),
AntQuestion("height", ["below", "breadth", "depth", "under"], "depth"),
AntQuestion("sober", ["combine", "displease", "drunk", "reveal"], "drunk"),
AntQuestion("foreign", ["native", "odd", "strange", "fortune"], "native"),
AntQuestion("obese", ["fertile", "large", "gaunt", "sudden"], "gaunt"),
AntQuestion("deny", ["doubt", "understand", "forbid", "confirm"], "confirm"),
AntQuestion("expand", ["grow", "contract", "rest", "enlarge"], "contract"),
AntQuestion("flow", ["scarce", "rush", "retreat", "ebb"], "ebb")

]

correct = 0
print(" ")
random.shuffle(questions)
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
        for x in range(30):
            print("ok"* x)
        print("---------------")
        correct = correct + 1
    else:
        print("---------------")
        print("correct answer: ", question.correct)
        print("---------------")

    raw_input("press any key to continue....")

print("correct: ", correct)
print("not correct: ", len(q) - correct)
