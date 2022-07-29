# 1.
"""
    This is my python program to Find the Factorial of a Number
"""
try:
    n = int(input('Enter a number : '))
    factorial = 1
    if n<0:
        print('Factorial for negative numbers is not available')
    elif n==0:
        print('Factorial for 0 is 1')
    else:
        for i in range(1,n+1):
            factorial = factorial*i
    print("Factorial of the number is : ", factorial)

except Exception as e:
    print(e)


# 2.
"""
    This is my python program to Display the multiplication Table
"""
n = int(input('Enter a number : '))
for i in range(1,11):
    print('',n,"*",'',i,"=",n*i)


# 3.
"""
    This is my python program to Print the Fibonacci sequence
"""
n = int(input('Enter the number of terms : '))
a, b = 0,1
count = 0
if n<0:
    print('Please enter a positive number')
elif n==1:
    print('Fibonacci sequence upto',n,' : ',a)
else:
    while count < n:
        print(a)
        fib = a+b
        a=b
        b=fib
        count+=1


# 4.
"""
    This is my python program to Check Armstrong Number
"""
num = int(input('Enter a number : '))
digits = len(str(num))
temp = num
new_num = 0
try:
    while temp != 0:
        rem = temp%10
        new_num += rem**digits
        temp = temp//10
except Exception as e:
    print(e)

if new_num == num:
    print('Given number is an armstrong number')
else:
    print("Given number is not an armstrong number")


# 5.
"""
    This is my python program to Find Armstrong Number in an Interval
"""
for num in range(100,1000):
    digits = len(str(num))
    temp = num
    new_num = 0
    while temp != 0:
        rem = temp%10
        new_num += rem**digits
        temp = temp//10

    if new_num == num:
        print(num)
    else:
        pass


# 6.
"""
    This is my python program to Check Armstrong Number?
"""
n = int(input('Enter a number : '))
sum = 0
for i in range(n+1):
    sum+=i

print(sum)