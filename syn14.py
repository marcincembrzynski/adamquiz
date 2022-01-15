import quiz

questions = [
quiz.NotSynQuestion(["support", "protest", "objection", "challenge"], "support"),
quiz.NotSynQuestion(["help", "aid", "hinder", "assist"], "hinder"),
quiz.NotSynQuestion(["attempt", "desperate", "try", "endeavour"], "desperate"),
quiz.NotSynQuestion(["wonder", "awe", "courage", "amazement"], "courage"),
quiz.NotSynQuestion(["sphere", "globe", "orb", "hemisphere"], "hemisphere"),
quiz.NotSynQuestion(["diameter", "width", "length", "breadth"], "length"),
quiz.NotSynQuestion(["assist", "hamper", "hinder", "impede"], "assist"),
quiz.NotSynQuestion(["alter", "church", "change", "modify"], "church"),
quiz.NotSynQuestion(["rubbish", "decline", "waste", "refuse"], "decline"),
quiz.NotSynQuestion(["right", "proper", "left", "just"], "left"),
quiz.NotSynQuestion(["ring", "core", "chime", "peal"], "core"),
quiz.NotSynQuestion(["strike", "hit", "beat", "mark"], "mark"),
quiz.NotSynQuestion(["study", "learn", "office", "bureau"], "learn"),
quiz.NotSynQuestion(["tariff", "duty", "tax", "deposit"], "deposit"),
quiz.NotSynQuestion(["ample", "abundant", "plentiful", "scarce"], "scarce"),
quiz.NotSynQuestion(["tears", "weep", "cry", "sob"], "tears"),
quiz.NotSynQuestion(["taunt", "tease", "jeer", "bluff"], "bluff"),
quiz.NotSynQuestion(["youthful", "senior", "adolescent", "juvenile"], "senior"),
quiz.NotSynQuestion(["hurried", "abrupt", "linger", "hasty"], "linger"),
quiz.NotSynQuestion(["edible", "acrid", "bitter", "sour"], "edible"),
quiz.NotSynQuestion(["accidental", "mindfully", "involuntary", "inadvertent"], "mindfully"),
quiz.NotSynQuestion(["enlarge", "minute", "magnify", "augment"], "minute"),
quiz.NotSynQuestion(["abandon", "ceasefire", "leave", "advance"], "advance"),
quiz.NotSynQuestion(["real", "copy", "genuine", "actual"], "copy")

]

quiz.Quiz(questions).test()
