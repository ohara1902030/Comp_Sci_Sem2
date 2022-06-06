mynumbersin = [6,9,32,28,15,22,3,18]
d = 0
for k in range(len(mynumbersin)):
    for h in range(len(mynumbersin)):
        if mynumbersin[k] >= mynumbersin[d]:
            d = d + 1
            