import quiz


questions = [

quiz.AntQuestion("feeble", ["tease", "permanent", "weak", "strong"], "strong"),
quiz.AntQuestion("foe", ["fiend", "faux", "friend", "fool"], "friend"),
quiz.AntQuestion("folly", ["fool", "wish", "wisdom", "kingdom"], "wisdom"),
quiz.AntQuestion("fickle", ["host", "loyal", "friend", "ferocious"], "loyal"),
quiz.AntQuestion("former", ["latent", "lament", "latter", "late"], "latter"),
quiz.AntQuestion("fragile", ["robot", "both", "robust", "bust"], "robust"),
quiz.AntQuestion("frail", ["rail", "strong", "weak", "trail"], "strong"),
quiz.AntQuestion("frivolous", ["fabulous", "absolute", "sensitive", "sensible"], "sensible"),
quiz.AntQuestion("gain", ["grain", "loss", "advantage", "reaction"], "loss"),
quiz.AntQuestion("glad", ["glide", "glut", "silly", "sorry"], "sorry"),
quiz.AntQuestion("goad", ["glad", "good", "bad", "pacify"], "pacify"),
quiz.AntQuestion("gobble", ["nibble", "noble", "gob", "grab"], "nibble"),
quiz.AntQuestion("graceful", ["gleeful", "grateful", "gull", "clumsy"], "clumsy"),
quiz.AntQuestion("gradual", ["grade", "good", "sudden", "sullen"], "sudden"),
quiz.AntQuestion("greatest", ["superlative", "less", "least", "leash"], "least")]

quiz.Quiz(questions).test()
