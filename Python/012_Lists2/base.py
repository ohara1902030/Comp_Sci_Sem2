import random
dlist = []
ue = int(input("How many numbers do you want to create?"))
for d in range(0,ue):
    dlist.append(random.randrange(0,10))
print("Your numbers are " + str(dlist))

