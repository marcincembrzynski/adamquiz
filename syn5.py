import quiz

questions = [
quiz.SynQuestion("high", ["leap", "loop", "lean", "lofty"], "lofty"),
quiz.SynQuestion("moisture", ["mellow", "dampness", "liquid", "most"], "dampness"),
quiz.SynQuestion("least", ["maximum", "mininum", "linger", "leisure"], "minimum"),
quiz.SynQuestion("dumb", ["bell", "mute", "pacify", "wild"], "mute"),
quiz.SynQuestion("disease", ["dealer", "health", "manage", "malady"], "malady"),
quiz.SynQuestion("fable", ["myth", "fail", "quote", "increase"], "myth"),
quiz.SynQuestion("most", ["damp", "maximum", "least", "average"], "maximum"),
quiz.SynQuestion("agile", ["agent", "decide", "nimble", "neccessary"], "nimble"),
quiz.SynQuestion("edge", ["under", "margin", "tense", "out"], "margin"),
quiz.SynQuestion("groan", ["grow", "group", "mow", "moan"], "moan"),
quiz.SynQuestion("rowdy", ["annoy", "noisy", "timid", "brave"], "noisy"),
quiz.SynQuestion("new", ["clean", "traditional", "modern", "frequent"], "modern"),
quiz.SynQuestion("choice", ["delegate", "compulsory", "option", "average"], "option"),
quiz.SynQuestion("peculiar", ["pretty", "amazing", "strange", "normal"], "strange"),
quiz.SynQuestion("plume", ["stone", "frequent", "feather", "placid"], "feather"),

]

quiz.Quiz(questions).test()
