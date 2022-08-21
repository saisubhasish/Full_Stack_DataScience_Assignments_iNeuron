# 1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?

"""
    This is my python program for Fibonacci number using recursion function
"""
import  logging
logging.basicConfig(filename='Programming_Assignment6.log', level=logging.INFO,
                            format='%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info("----------------------------------------------------------------------------")

try:
    def recurssive(n):
        if n <= 1:
            return n
        else:
            return (recurssive(n-1) + recurssive(n-2))

except Exception as e:
    logging.exception(e)

n = int(input('Enter the number of fibonacci number you want : '))
try:
    if n <= 0:
        print("Please enter a positive number")
    else:
        for i in range(n):
            print(recurssive(i))

except Exception as e:
    logging.exception(e)

logging.info("----------------------------------------------------------------------------")

# 2.	Write a Python Program to Find Factorial of Number Using Recursion?

"""
    This is my python program for Factorial of Number using recursion function
"""

def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)

n = int(input('Enter a number : '))
if n < 0:
    print("Factorial does not exists for negative numbers")
elif n==0:
    logging.info("The factorial of 0 is 1")
else:
    logging.info("The factorial of ",n," is : ", fact(n))

logging.info("----------------------------------------------------------------------------")

# 3.	Write a Python Program to calculate your Body Mass Index?

"""
    This is my python program to calculate your Body Mass Index
"""

try:
    def BMI(weight, height):
        bmi = weight/(height**2)
        return bmi

except Exception as e:
    logging.exception(e)

weight = int(input("Enter weight in kg : "))
height = float(input("Enter height in meter : "))

bmi = BMI(weight, height)
logging.info("The BMI is : ",format(bmi), "so", end=' ')

if (bmi<18.5):
    logging.info("Under Weight")

elif (bmi >= 18.5 and bmi < 24.9):
    logging.info("Healthy")

elif (bmi >= 24.9 and bmi<30):
    logging.info("Over Weight")

elif (bmi >= 30):
    logging.info("Suffering from Obesity")

logging.info("----------------------------------------------------------------------------")

# 4.	Write a Python Program to calculate the natural logarithm of any number

"""
    This is my python program to calculate the natural logarithm of any number
"""
import math

def logarith(n):
    if n < 0:
        print("Enter a positive number")
    else:
        print("Logarithm of {}".format(n)," is : ",math.log(n))

n = int(input("Enter a number : "))
logarith(n)

logging.info("----------------------------------------------------------------------------")

# 5.	Write a Python Program for cube sum of first n natural numbers?

"""
    This is my python program for cube sum of first n natural numbers
"""
def cube_sum(n):
    if n <= 0:
        print("Enter a positive number")
    else:
        sum = 0
        for i in range(n+1):
            sum += i**3
    return sum

n = int(input("Enter a number : "))
logging.info(cube_sum(n))

logging.info("----------------------------------------------------------------------------")