#recursion is basically a function calling itself multiple times
def Factorial(num):   
    if num == 1:
        return 1
    return num * Factorial(num - 1)

number = 4
print(Factorial(number))
 
#4 * Factorial(3)
#3 * Factorial(2)
#2 * Factorial(1)
#1

def Fibonnaci(num):
    if num <= 1:
        return 1
    return Fibonnaci(num - 1) + Fibonnaci(num - 2)

number = 5
print(Fibonnaci(number))
