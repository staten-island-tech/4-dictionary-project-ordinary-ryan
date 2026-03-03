


""" def occupied(x,y,t):
    found= 0
    for i in range(x):
        if y[i] == "c" and t[i] == "c":
            found += 1
    print(found)
occupied (5, "c.ccc", "c.c.c")
 """

""" def lang(sent):
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

lang("The red cat sat on the mat. Why are you so sad cat? Don't ask that") """


def lang(sent):
    h= 0
    for i in sent:
        if i == "H":
            h += 0
        elif i == "O" and i == "H":
            h += 0
        elif i == "O" and i == "H" and i == "N":
            h +=0 
        elif i == "O" and i == "H" and i == "N" and i == "I":
            h += 1
    honi_count = h
    print(honi_count)
    
lang("PROHODNIHODNIK")
""" for i in sent:
        if i == "H":
            h += 1
        elif i == "O" :
            o += 1
        elif i == "N" :
            n += 1
        elif i == "I":
            e += 1
        
            honi_count = (h + o + n + e) / 4
        print(honi_count) """