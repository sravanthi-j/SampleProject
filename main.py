# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Dashboard import Square


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

x=int(input('Enter 1st number: '))
y=int(input('Enter 2nd number: '))
operand=input('Enter the operation Add/Sub/Mul/Div: ')

    if operand == "+":
        print(x + y)
    elif operand == "-":
        print  (x - y)
    elif operand == "*":
        print (x * y)
    else:
        print  (x // y)



def Sravanthi(FullName):
    print('Hi i am ' + FullName)
# Press the green button in the gutter to run the script.

    rootNumber=input('Please enter  a numer to find Square ' )
    Square_Number=Square(int(rootNumber))
    print('Square of ' + str(rootNumber) + ' is ' + str(Square_Number))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

