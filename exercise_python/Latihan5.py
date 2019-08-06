# Lets try making a calculator using input argument

print("Let's count something.")
op1 = int(input('Input your first number > '))
op2 = int(input('Input your second number > '))

print('Choose your operation!\n 1 = addition\n 2 = substraction\n 3 = multiplication\n 4 = division')
operation = int(input('> '))

    if operation == 1:
        print('The result of', op1, 'plus', op2, 'is', op1 + op2)
    elif operation == 2:
        print('The result of', op1, 'minus', op2, 'is', op1 - op2)
    elif operation == 3:
        print('The result of', op1, 'multiplied by', op2, 'is', op1 * op2)
    elif operation == 4:
        print('The result of', op1, 'divided by', op2, 'is', op1 / op2)
    else:
        print('Unkown error.')

