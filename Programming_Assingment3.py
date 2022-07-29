# 1.
"""
    This is my python program to Check if a Number is Positive, Negative or Zero
"""
n = int(input('Enter a number : '))
if n>0:
    print('It is a positive number : ',n)
elif n<0:
    print('It is a negative number : ',n)
elif n==0:
    print('This number is zero  : ',n)
else:
    print('Please enter a valid number : ',n)


# 2.
"""
    This is my python program to Check if a Number is Positive, Negative or Zero
"""
n = int(input('Enter a number : '))
if n%2==0:
    print('It is an Even number : ',n)
else:
    print('It is an Odd number : ',n)


# 3.
"""
    This is my python program to Check Leap Year
"""
year = int(input('Enter a year : '))
if (year%400==0) and (year%100==0):
    print('{0} is a leap year'.format(year))
elif (year%4==0) and (year%100!=0):
    print('{a} is a leap year'.format(a=year))
else:
    print('{z} is not a leap year'.format(z=year))


# 4.
"""
    This is my python program to Check Prime number
"""
try:
    n = int(input('Enter a number : '))
    if n <= 1:
        print('Not a prime number : ',n)
    elif n>1:
        for i in range(2,int(n/2)+1):
            if n%i == 0:
                print('Not a prime number : ',n)
                break
        else:
            print('It is a prime number : ',n)

    else:
        print('Not a prime number : ',n)

except Exception as e:
    print(e)


# 5.
"""
    This is my python program to Print all Prime Numbers in an Interval of 1-10000
"""
try:
    for n in range (1,10000):
        if n <= 1:
            pass
        elif n>1:
            for i in range(2,int(n/2)+1):
                if n%i == 0:
                    break
            else:
                print(n)
except Exception as e:
    print(e)
