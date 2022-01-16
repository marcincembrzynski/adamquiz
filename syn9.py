import quiz

questions = [
quiz.SynQuestion("construct", ["allow", "build", "debate", "demolish"], "build"),
quiz.SynQuestion("persuade", ["convince", "pressure", "agree", "allow"], "convince"),
quiz.SynQuestion("recall", ["telephone", "retain", "remember", "shout"], "remember"),
quiz.SynQuestion("weary", ["weird", "clothes", "tired", "excited"], "tired"),
quiz.SynQuestion("dilligent", ["silly", "lazy", "slow", "hardworking"], "hardworking"),
quiz.SynQuestion("assault", ["attack", "condiment", "embrace", "flee"], "attack"),
quiz.SynQuestion("tepid", ["treatment", "scary", "tired", "lukewarm"], "lukewarm"),
quiz.SynQuestion("ponder", ["consider", "worry", "talk", "boast"], "consider"),
quiz.SynQuestion("remain", ["leave", "stay", "depart", "part"], "stay"),
quiz.SynQuestion("disperse", ["scatter", "combine", "displease", "gather"], "scatter"),
quiz.SynQuestion("odour", ["order", "ordeal", "smell", "small"], "smell"),
quiz.SynQuestion("abrupt", ["slowly", "kind", "abroad", "sudden"], "sudden"),
quiz.SynQuestion("brief", ["build", "understand", "short", "long"], "short"),
quiz.SynQuestion("reluctant", ["willing", "unwilling", "distrust", "lucky"], "unwilling"),
quiz.SynQuestion("loathe", ["love", "like", "hate", "keen"], "hate")

]

quiz.Quiz(questions).test()
