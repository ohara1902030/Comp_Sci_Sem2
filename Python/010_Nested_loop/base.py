symbol = str(input("Enter the symbol you want to be used for the box"))
length = int(input("Enter line length > "))
width = int(input("Enter box width? > "))



for x in range(0,length):
    for c in range(0, width):
        if(x == 0 or x == length-1 or c == 0 or c == width-1):
            print(symbol, end= " ")
        else:
            print(" ", end= " ")
    print()

