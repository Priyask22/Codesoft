print("1. Addition")
print("2 Subtraction")
print("3 Multipication")
print("4 Division")

option=int(input("Chose a operation"))

if(option in [1,2,3,4]):
    num1=int(input("enter first number"))
    num2=int(input("Enter second number"))

    if(option==1):
        res=num1+num2
    elif(option==2):
        res=num1-num2
    elif (option == 3):
        res = num1 *num2
    elif (option == 4):
        res = num1 / num2

    else:
        print("invalid")

print(res)


