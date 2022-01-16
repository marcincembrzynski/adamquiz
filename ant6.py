import quiz

questions = [
quiz.AntQuestion("transparent", ["opaque", "clear", "genuine", "bright"], "opaque"),
quiz.AntQuestion("plain", ["fancy", "easy", "simple", "hard"], "fancy"),
quiz.AntQuestion("pedestrian", ["climber", "walker", "pilot", "motorist"], "motorist"),
quiz.AntQuestion("hero", ["coward", "simple", "adult", "infant"], "coward"),
quiz.AntQuestion("giant", ["glad", "massive", "dwarf", "jolly"], "dwarf"),
quiz.AntQuestion("unknown", ["fancy", "condiment", "well", "famous"], "famous"),
quiz.AntQuestion("smile", ["grin", "frown", "mouth", "pout"], "frown"),
quiz.AntQuestion("generous", ["consider", "mean", "kind", "boast"], "mean"),
quiz.AntQuestion("height", ["below", "breadth", "depth", "under"], "depth"),
quiz.AntQuestion("sober", ["combine", "displease", "drunk", "reveal"], "drunk"),
quiz.AntQuestion("foreign", ["native", "odd", "strange", "fortune"], "native"),
quiz.AntQuestion("obese", ["fertile", "large", "gaunt", "sudden"], "gaunt"),
quiz.AntQuestion("deny", ["doubt", "understand", "forbid", "confirm"], "confirm"),
quiz.AntQuestion("expand", ["grow", "contract", "rest", "enlarge"], "contract"),
quiz.AntQuestion("flow", ["scarce", "rush", "retreat", "ebb"], "ebb")]

quiz.Quiz(questions).test()
