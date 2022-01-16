import quiz

questions = [
quiz.AntQuestion("thrifty", ["fast", "extravagant", "mean", "fifty"], "extravagant"),
quiz.AntQuestion("pompous", ["humble", "hurt", "mellow", "magical"], "humble"),
quiz.AntQuestion("prosper", ["gain", "rich", "deny", "fail"], "fail"),
quiz.AntQuestion("join", ["sever", "meet", "severe", "several"], "sever"),
quiz.AntQuestion("sunny", ["damp", "cloudy", "foggy", "misty"], "cloudy"),
quiz.AntQuestion("innocence", ["order", "mend", "guilt", "hurt"], "guilt"),
quiz.AntQuestion("pacify", ["calm", "rectify", "please", "annoy"], "annoy"),
quiz.AntQuestion("enlarged", ["reduced", "increased", "dispersed", "released"], "reduced"),
quiz.AntQuestion("bow", ["bend", "stern", "straight", "strain"], "stern"),
quiz.AntQuestion("callous", ["kind", "calm", "practical", "wicked"], "kind"),
quiz.AntQuestion("cause", ["reason", "emit", "effect", "enlarge"], "effect"),
quiz.AntQuestion("assist", ["help", "hinder", "manage", "defer"], "hinder"),
quiz.AntQuestion("elated", ["happy", "serious", "glad", "sad"], "sad"),
quiz.AntQuestion("expose", ["keep", "watch", "enlarge", "hide"], "hide"),
quiz.AntQuestion("coy", ["bold", "timid", "cry", "aware"], "bold")]


quiz.Quiz(questions).test()
