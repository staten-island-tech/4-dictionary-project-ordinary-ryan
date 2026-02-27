


def occupied(x,y,t):
    found= 0
    for i in range(x):
        if y[i] == "c" and t[i] == "c":
            found += 1
    print(found)
occupied (5, "c.ccc", "c.c.c")
