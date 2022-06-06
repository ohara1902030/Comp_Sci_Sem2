x = int(input("How many items are you purchasing? > "))

total = 0
for c in range(0,x):
   t = input(("What item are you buying? > "))
   a = float(input(("How much does " + t + " cost? > ")))
   total = total + a

print("Your total is: " + str(total))
