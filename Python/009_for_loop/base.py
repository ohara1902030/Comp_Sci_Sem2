length = int(input("Enter line length > "))
orient = str(input("Do you want the line to be horizontal or vertical? > "))



if orient == ("horizontal"):
    for x in range(0,length):
        print("*", end="")
    
elif orient == ("vertical"):
    for x in range(0,length):
        print("*")

else:
    print("Invalid orientation.")
