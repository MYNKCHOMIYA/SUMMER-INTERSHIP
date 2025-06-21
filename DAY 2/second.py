a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = input("enter +, - ,* , / , % : ")

if c=="+":
     print(f"sum is  = {a + b}")
elif c=="-":
    print(f"difference is =  {a - b}")
elif c == "*":
    print(f"multiply is = {a * b}")
elif c == "/":
    print(f"div is = {a / b}")
elif c == "%":
    print(f"modules is = {a % b}")
else:
    print("invalid operator")
