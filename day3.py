a=int(input("enter a first number:"))
b=int(input("enter a second number"))
c=input("enter the operator:")
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
else:
    print("invalid operator")