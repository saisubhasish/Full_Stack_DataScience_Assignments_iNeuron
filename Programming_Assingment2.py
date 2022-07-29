# 1.
"""
    This is my python program to convert kilometers to miles
"""
km = int(input('Enter the distance in kilometers : '))
print('Distance in miles : ', km*0.62137, "miles")


# 2.
"""
    This is my python program to convert kilometers to miles
"""
c = int(input('Enter the temperature in Celsius : '))
print('Temperature in Fahrenheit : ', ((c*9/5)+32), "°F")


# 3.
"""
    This is my python program to display calendar
"""
import calendar

year = int(input('Enter the year : '))
month = int(input("Enter the month : "))
print(calendar.month(year , month))


# 4.
"""
    This is my python program to solve quadratic equation
"""
import cmath

a = int(input('Enter first integer value : '))
b = int(input('Enter second integer value : '))
c = int(input('Enter third integer value : '))
d = (b**2) - (4*a*c)
qeN = (-b-cmath.sqrt(d))/(2*a)
qeP = (-b+cmath.sqrt(d))/(2*a)
print('The positive value for Quadratic equation is : {a} and negative value is : {b}'.format(b = qeP , a = qeN))


# 5.
"""
    This is my python program to swap two variables without temp variable
"""
a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
a = a+b
b = a-b
a = a-b
print('After swapping the updated value of first number is : {0} and second number is : {1}'.format(a,b))