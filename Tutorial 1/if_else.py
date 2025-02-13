def Calculate(first, second, op):
    if op == '+' :
        return first + second
    elif op == '-':
        return first - second
    elif op == '*':
        return first * second
    elif op == '/':
        if second_number !=0:  ##and second_number >= 1:(a)
            return first / second
        else:
            return 'Cannot divide by zero'
    else:
        return 'Please enter a valid operation'
    

first_number = float(input('Please enter the first number: '))
second_number = float(input('Please enter the second number: '))
operation = input('Please enter an operation: ')
result = Calculate(first_number, second_number)
print(result)

#Match case useful when you have if conditions that are straight forward
def Calculate(first, second, op):
    match op:
        case '+':
            return first + second
        case '-':
            return first - second
        case '*':
            return first * second
        case '/':
            if second ! = 0:
            return first / second
            else:
                return 'division by zero error'
        case _:
            return 'Something went wrong'
            
first_number = float(input('Please enter the first number: '))
second_number = float(input('Please enter the second number: '))
operation = input('Please enter an operation: ')
result = Calculate(first_number, second_number)
print(result)

