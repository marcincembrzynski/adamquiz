import quiz

questions = [
quiz.AntQuestion("artificial", ["allow", "genuine", "debate", "demolish"], "genuine"),
quiz.AntQuestion("plural", ["convince", "detract", "singular", "allow"], "singular"),
quiz.AntQuestion("poverty", ["wealth", "retain", "remember", "present"], "wealth"),
quiz.AntQuestion("compulsory", ["weird", "voluntary", "tired", "excited"], "voluntary"),
quiz.AntQuestion("diligent", ["silly", "lazy", "slow", "hardworking"], "lazy"),
quiz.AntQuestion("permanent", ["attack", "condiment", "temporary", "flee"], "temporary"),
quiz.AntQuestion("reward", ["treatment", "discipline", "tired", "punishment"], "punishment"),
quiz.AntQuestion("deny", ["condider", "worry", "admit", "boast"], "admit"),
quiz.AntQuestion("severe", ["leave", "stay", "depart", "mild"], "mild"),
quiz.AntQuestion("conceal", ["combine", "displease", "gather", "reveal"], "reveal"),
quiz.AntQuestion("tranquil", ["order", "ordeal", "smell", "rough"], "rought"),
quiz.AntQuestion("barren", ["fertile", "kind", "abroad", "sudden"], "fertile"),
quiz.AntQuestion("permit", ["build", "understand", "forbid", "long"], "forbid"),
quiz.AntQuestion("foolish", ["willing", "unwilling", "resistant", "wise"], "wise"),
quiz.AntQuestion("frightened", ["scarce", "calm", "retreat", "leave"], "calm")]

quiz.Quiz(questions).test()
