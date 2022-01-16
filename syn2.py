import quiz

questions = [
quiz.SynQuestion("drowsy" , ["awake", "cross", "sleepy", "active"], "sleepy"),
quiz.SynQuestion("depart", ["arrive", "decide", "slice", "leave"], "leave"),
quiz.SynQuestion("peril", ["safety", "extreme", "security", "danger"], "danger"),
quiz.SynQuestion("plucky", ["brave", "clever", "safety", "crazy"], "brave"),
quiz.SynQuestion("assist", ["hinder", "help", "manage", "cheat"], "help"),
quiz.SynQuestion("interior", ["design", "interest", "inside", "increase"], "inside"),
quiz.SynQuestion("end", ["depart", "gallop", "stop", "arrive"], "stop"),
quiz.SynQuestion("hasten", ["wait", "hurry", "leave", "tie"], "hurry"),
quiz.SynQuestion("descend", ["part", "go down", "go up", "spread"], "go down"),
quiz.SynQuestion("commence", ["begin", "stop", "business", "allowance"], "begin"),
quiz.SynQuestion("bold", ["dim", "hairless", "timid", "brave"], "hairless"),
quiz.SynQuestion("comprehend", ["manage", "understand", "realise", "listen"], "understand"),
quiz.SynQuestion("deteriorate", ["improve", "worsen", "detach", "damage"], "worsen"),
quiz.SynQuestion("many", ["multiply", "receive", "single", "numerous"], "numerous"),
quiz.SynQuestion("contemporary", ["former", "current", "traditional", "old"], "current")

]

quiz.Quiz(questions).test()
