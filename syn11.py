import quiz

questions = [
quiz.SynQuestion("robust", ["weak", "strong", "lean", "lively"], "strong"),
quiz.SynQuestion("site", ["mellow", "vintage", "scene", "score"], "scene"),
quiz.SynQuestion("shrine", ["tomb", "shrink", "boat", "grave"], "tomb"),
quiz.SynQuestion("sleek", ["smooth", "weak", "snooze", "rough"], "smooth"),
quiz.SynQuestion("slender", ["dealer", "slim", "bend", "shake"], "slim"),
quiz.SynQuestion("squirm", ["shrink", "wail", "screech", "wriggle"], "wriggle"),
quiz.SynQuestion("steed", ["deer", "horse", "goat", "pig"], "horse"),
quiz.SynQuestion("stern", ["lenient", "storm", "strict", "chimmey"], "strict"),
quiz.SynQuestion("stubborn", ["obstinate", "control", "tense", "infant"], "obstinate"),
quiz.SynQuestion("sturdy", ["flexible", "stuck", "strong", "weak"], "strong"),
quiz.SynQuestion("surrender", ["yield", "give back", "frugal", "advance"], "yield"),
quiz.SynQuestion("suspend", ["accept", "hang", "convert", "frequent"], "hang"),
quiz.SynQuestion("terror", ["anxious", "dog", "option", "fear"], "fear"),
quiz.SynQuestion("tested", ["exam", "tried", "strange", "normal"], "tried"),
quiz.SynQuestion("thrust", ["leap", "tense", "pushed", "placid"], "pushed")

]

quiz.Quiz(questions).test()
