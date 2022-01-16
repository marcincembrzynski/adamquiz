import quiz

questions = [
quiz.SynQuestion("deluge", ["destroy", "flood", "scatter", "scold"], "flood"),
quiz.SynQuestion("detest", ["hate", "leave", "bread", "heave"], "hate"),
quiz.SynQuestion("forbidden", ["allowed", "prohibited", "forever", "ignore"], "prohibited"),
quiz.SynQuestion("deliberately", ["purposely", "definitely", "sparingly", "fully"], "purposely"),
quiz.SynQuestion("rectify", ["release", "maintain", "decide", "correct"], "correct"),
quiz.SynQuestion("rigid", ["subtle", "flexible", "stiff", "right"], "stiff"),
quiz.SynQuestion("strenous", ["straight", "vigorous", "easy", "light"], "vigorous"),
quiz.SynQuestion("sceptical", ["serious", "believing", "worrying", "unbeliewing"], "unbeliewing"),
quiz.SynQuestion("reside", ["live", "across", "opposite", "resident"], "live"),
quiz.SynQuestion("resist", ["withstand", "without", "withdraw", "wither"], "withstand"),
quiz.SynQuestion("submissive", ["obedient", "obnoxious", "obstinate", "obstruct"], "obedient"),
quiz.SynQuestion("profound", ["proof", "deep", "discover", "width"], "deep"),
quiz.SynQuestion("prudent", ["sorry", "perfect", "worry", "wise"], "wise"),
quiz.SynQuestion("interrogate", ["question", "intact", "elevate", "medidate"], "question"),
quiz.SynQuestion("mature", ["young", "ripe", "lessen", "control"], "ripe")

]

quiz.Quiz(questions).test()
