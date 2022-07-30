# 1.
"""
    This is my python program to Find LCM
"""
def findLCM(a,b):
    if a>b:
        greater = a
    else:
        greater = b
    while (True):
        if (greater%a == 0) and (greater%b == 0):
            lcm = greater
            break
        greater+=1
    return lcm

print(findLCM(int(input('Enter first number : ')),int(input('Enter second number : '))))


# 2.
"""
    This is my python program to Find HCF
"""
def findHCF(a,b):
    if a<b:
        smaller = a
    else:
        smaller = b
    for i in range(1,smaller+1):
        if (a%i==0) and (b%i==0):
            hcf = i
    return hcf
print(findHCF(int(input('Enter first number : ')),int(input('Enter second number : '))))


# 3.
"""
    This is my python program to Convert Decimal to Binary, Octal and Hexadecimal
"""
dec = int(input('Enter a decimal number : '))
print('The decimal value is : ', dec)
print('The converted binary value of',dec,'is : ', bin(dec))
print('The converted octal value of',dec,'is : ', oct(dec))
print('The converted hexadecimal value of',dec,'is : ', hex(dec))


# 4.
"""
    This is my python program to Convert Decimal to Find ASCII value of a character
"""
ch = input('Enter a character : ')
print('The ASCII value of',ch,'is : ',ord(ch))


# 5.
"""
    This is my python program to Make a Simple Calculator with 4 basic mathematical operations
"""
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print('List of perations :')
print('1 - Addition')
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

while True:
    choice = int(input('Enter the choice of operation you want to perform (1/2/3/4): '))
    if choice in (1,2,3,4):
        num1 = int(input('Enter the first number : '))
        num2 = int(input('Enter the second number : '))
        if choice == 1:
            print(num1,'+',num2,'=',add(num1,num2))
        elif choice == 2:
            print(num1,'-',num2,'=',sub(num1,num2))
        elif choice == 3:
            print(num1,'*',num2,'=',mul(num1,num2))
        elif choice == 4:
            print(num1,'/',num2,'=',div(num1,num2))

        next_operation = input('Do you want to do next calculation? (yes/no): ')
        operation = next_operation.lower()
        if operation == 'no':
            break
    else:
        print('Invalid input')

