import quiz

questions = [
quiz.AntQuestion("accidental", ["rental", "liberate", "mistake", "deliberate"], "deliberate"),
quiz.AntQuestion("active", ["octave", "passive", "positive", "present"], "passive"),
quiz.AntQuestion("admiration", ["flotation", "admiral", "contempt", "contemplate"], "contempt"),
quiz.AntQuestion("aggrevate", ["alleviate", "raise", "lower", "aggregate"], "alleviate"),
quiz.AntQuestion("artful", ["tearless", "heartless", "artless", "artistic"], "artless"),
quiz.AntQuestion("attractive", ["substracted", "divided", "responsive", "repulsive"], "repulsive"),
quiz.AntQuestion("beneficial", ["fiscal", "harmful", "financial", "necessity"], "harmful"),
quiz.AntQuestion("blame", ["praise", "bloat", "precise", "passive"], "praise"),
quiz.AntQuestion("bravery", ["stupidity", "intelligence", "cowardice", "risk"], "cowardice"),
quiz.AntQuestion("brief", ["brie", "absurd", "lengthy", "short"], "lengthy"),
quiz.AntQuestion("build", ["construct", "demon", "concave", "demolish"], "demolish"),
quiz.AntQuestion("captive", ["free", "advance", "defence", "offend"], "free"),
quiz.AntQuestion("cherish", ["love", "hate", "like", "intolerable"], "hate"),
quiz.AntQuestion("clemency", ["enforce", "isolate", "insulate", "sufficient"], "enforce"),
quiz.AntQuestion("coax", ["persuade", "compel", "pursue", "discourage"], "discourage")
]


quiz.Quiz(questions).test()
