x = int(input("Enter first number"))
y = int(input("Enter second number"))
z = input("Enter operator")

q = x * y
w = x + y
e = x - y
r = x / y



if z == "*":
    print(q)
elif z == "+":
    print (w)
elif z == "-":
    print(e)
elif z == "/":
    print(r)
else:
    print("Invalid Operator")