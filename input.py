#!/bin/python3
print("=======================================")
x = float(input("give me a a number: "))
o = input("Give an opertor: ")
y = float(input("Give me yet another number: "))
if o == "+":
    print(x+y)

elif o == "-":
    print(x-y)

elif o == "*":
    print(x*y) 

elif o == "/":
    print(x/y)

elif o == "**":
        print(x**y)

else:
        print("Uknow operator.")        