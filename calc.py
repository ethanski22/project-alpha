import operator

#define operators you wanna use
allowed_operators={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
		'%' : operator.mod,
    '^' : operator.xor}

#sample variables
num1 = int(input("Enter a num: "))
num2 = int(input("Enter a num: "))
what = input("What do you want to do\nplease type exactly what you see\n+ - * / % ^    ")

#sample calculation => a+b
result=allowed_operators[what](num1,num2)
print(result)