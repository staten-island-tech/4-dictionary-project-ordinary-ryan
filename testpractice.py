


""" def occupied(x,y,t):
    found= 0
    for i in range(x):
        if y[i] == "c" and t[i] == "c":
            found += 1
    print(found)
occupied (5, "c.ccc", "c.c.c")
 """

def lang(sent):
        s = 0
        t = 0
        for i in sent:
            if i == "t" or i == "T":
                t += 1
            elif i == "s" or i == "S":
                s += 1
        
        if s >= t:
            print("this text is probably french")
        else:
            print("this is likely english")

lang("The red cat sat on the mat. Why are you so sad cat? Don't ask that")

""" def lang(sent):
    s = 0
    t = 0
    for i in sent:
        if i == "s" or i == "S":
               s += 1
        elif i == "t" or i == "T"
 """