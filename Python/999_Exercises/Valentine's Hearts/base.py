import datetime


people_list = []
with open('People.txt') as f:
    for line in f:
        l = line.strip()
        people_list.append(l)

compliment_list = []
with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        compliment_list.append(l)
        
import random
pddd = random.randrange(0,len(people_list))
cddd = random.randrange(0,len(compliment_list))

print(people_list[pddd] + " " + compliment_list[cddd])


x = datetime.datetime.now()

print()
print("The date and time are:")
print(str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " at " + str(x.hour))

f.close()
