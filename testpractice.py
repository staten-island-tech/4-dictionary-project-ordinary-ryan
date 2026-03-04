


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

""" 
def lang(sent):
    h= True 
    for i in sent:
        if i == "H":
            h = False
        elif i == "H" and i == "O":
            h == False
        elif i == "H" and i == "O" and i == "N":
            h == False
        elif i == "H" and i == "O" and i == "N" and i == "I":
            h == True
            
    if h == True:
        h += 1
        print(h)
    
lang("MAGNUS") """

""" 
def lang(sent):
    h= 0
    o=0
    n=0
    e=0
    for i in sent:
        if i == "H":
            h += 1
        elif i == "H" and i == "O":
            h += 1
        elif i == "H" and i == "O" and i == "N":
            h += 1
        elif i == "H" and i == "O" and i == "N" and i == "I":
            h += 1
      

    honi_count = (h + o + n + e) // 4
    print(honi_count) 
lang("PROHODNIHODNIK") """

""" elif i == "O" :
            o += 1
        elif i == "N" :
            n += 1
        elif i == "I":
            e += 1 """
def magnus(word):
    count = 0
    state = 0
    for char in word:
        if state == 0 and char.upper() == "H":
            state = 1
        elif state == 1 and char.upper() == "O":
            state == 2
        elif state == 2 and char.upper() == "N":
            state =3
        elif state == 4 and char.upper() == "I":
            state = 0
            count += 1
    print(count)
magnus("HONI")