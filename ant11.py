import quiz

questions = [
quiz.AntQuestion("divided", ["unintented", "united", "dividend", "untied"], "united"),
quiz.AntQuestion("definite", ["effeminate", "finite", "defined", "doubtful"], "doubtful"),
quiz.AntQuestion("drought", ["draught", "nought", "flood", "ought"], "flood"),
quiz.AntQuestion("eager", ["ogre", "reluctant", "recluse", "resolve"], "reluctant"),
quiz.AntQuestion("economical", ["wasteful", "numeral", "apolitical", "mystical"], "wasteful"),
quiz.AntQuestion("economise", ["connotation", "squish", "squander", "square"], "squander"),
quiz.AntQuestion("elaborate", ["explain", "simple", "elastic", "sample"], "simple"),
quiz.AntQuestion("elated", ["lasted", "late", "arrive", "despondent"], "despondent"),
quiz.AntQuestion("extravagant", ["flendish", "frugal", "extraordinary", "extremely"], "frugal"),
quiz.AntQuestion("emerge", ["appear", "margarine", "disappear", "merge"], "disappear"),
quiz.AntQuestion("emigrate", ["grate", "great", "grater", "immigrate"], "immigrate"),
quiz.AntQuestion("engage", ["gauge", "dismay", "dismiss", "gaunt"], "dismiss"),
quiz.AntQuestion("evergreen", ["green", "ever", "never", "decidous"], "decidous"),
quiz.AntQuestion("exclude", ["execute", "dilute", "dissuade", "include"], "include"),
quiz.AntQuestion("exhale", ["hail", "inhale", "inter", "outer"], "inhale")
]


quiz.Quiz(questions).test()
