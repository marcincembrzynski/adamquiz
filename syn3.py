import quiz

questions = [
quiz.SynQuestion("dear", ["generous", "mean", "expensive", ""], "expensive"),
quiz.SynQuestion("buy", ["take", "give", "purchase", ""], "purchase"),
quiz.SynQuestion("give", ["borrow", "donate", "lend", ""], "donate"),
quiz.SynQuestion("pale", ["light", "dear", "cheap", ""], "light"),
quiz.SynQuestion("mediocre", ["massive", "slight", "slender", ""], "slight"),
quiz.SynQuestion("shiny", ["mild", "dim", "bright", ""], "bright"),
quiz.SynQuestion("depart", ["stay", "come", "go", ""], "go"),
quiz.SynQuestion("sour", ["salty", "sharp", "smooth", ""], "sharp"),
quiz.SynQuestion("concise", ["long", "case", "brief", ""], "brief"),
quiz.SynQuestion("informal", ["casual", "punctual", "late", ""], "casual"),
quiz.SynQuestion("occurence", ["immediate", "manage", "instance", ""], "instance"),
quiz.SynQuestion("liberty", ["freedom", "pass", "aloud", ""], "freedom"),
quiz.SynQuestion("enlarge", ["glass", "decrease", "magnify", ""], "magnify"),
quiz.SynQuestion("neccessary", ["request", "denied", "required", ""], "required"),
quiz.SynQuestion("proof", ["court", "evidence", "guilty", ""], "evidence"),
quiz.SynQuestion("inspect", ["examine", "lesson", "test", ""], "examine"),
quiz.SynQuestion("dive", ["plunge", "swim", "stroke", ""], "plunge"),
quiz.SynQuestion("significant", ["bizzare", "meaningful", "cleaver", ""], "meaningful"),
quiz.SynQuestion("proceed", ["continue", "retreat", "arrive", ""], "continue"),
quiz.SynQuestion("essential", ["needless", "random", "imperative", ""], "imperative")

]

quiz.Quiz(questions).test()
