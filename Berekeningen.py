import time
import os
def clear():
    command = 'cls'
    os.system(command)

clear()
def calc1():
    print('This will add both numbers together:')
    number1 = int(input('What is number 1?: '))
    number2 = int(input('What is number 2?: '))
    outcome1 = number1 + number2

    print('This will subtract your second number from the first:')
    number3 = int(input('What is number 3?: '))
    number4 = int(input('What is number 4?: '))
    outcome2 = number3 - number4

    print('This will multiply your numbers:')
    number5 = int(input('What is number 5?: '))
    number6 = int(input('What is number 6?: '))
    outcome3 = number5 * number6
    
    print(str(number1) + ' + ' + str(number2) + ' = ' + str(outcome1)) 
    print(str(number3) + ' - ' + str(number4) + ' = ' + str(outcome2))
    print(str(number4) + ' * ' + str(number5) + ' = ' + str(outcome3))


def calc2():
    print('This will divide your first number by the second')
    number7 = int(input('What is number 7?: '))
    number8 = int(input('What is number 8?: '))
    outcome4 = number7 / number8

    print('This will add one to your number')
    number9 = int(input('What is number 9?: '))
    outcome5 = number9 + 1

    print('This will subtract one from your number')
    number10 = int(input('What is number 10?: '))
    outcome6 = number10 - 1

    print(str(number7) + ' : ' + str(number8) + ' = ' + str(outcome4))
    print(str(number9) + ' + 1 = '  ' = ' + str(outcome5))
    print(str(number10) + ' - 1 = ' + str(outcome6))

calc1()
calc2()
