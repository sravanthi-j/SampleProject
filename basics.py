
def calculate_numbers(n1,n2,operator):
    if operator=='+':
        return int(n1)+int(n2)
    elif operator=='-':
        return int(n1)-int(n2)
    elif operator=='*':
        return int(n1)*int(n2)
    elif operator=='/':
        return int(n1)//int(n2)
    else:
        print('Invalid operator')

def display_data(n1):
(n1)+10=10
    name='sravnthi'
    print('The value of N1 is ' + str(n1))
    print('The value of Number1 is ' + str(Number1))

print('Please enter 2 numbers one by one ')
Number1=input('Please enter 1st number : ')
Number2=input('Please enter 2nd number : ')
Operand=input('Please enter the Operator : ')
result=calculate_numbers(Number1,Number2,Operand)
print('The ' + Operand + ' result of '  + Number1 + ' and ' + Number2 + ' is ' + str(result))




