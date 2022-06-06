FullName = input("What is your full name? ")
d = FullName[0:len(FullName)]
for d2 in range(0,len(FullName)):
    deitz = FullName[d:d+1]
    print(deitz)
    print(" ")
    
#Error is that in line 4, it takes the +1 as an int. 
#does not function