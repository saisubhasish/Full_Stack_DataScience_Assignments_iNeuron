# 1. No the Python Standard Library didn't include PyInputPlus.

# 2. PyInputPlus commonly imported with import pyinputplus as pypi so that you can enter a shorter name when calling
#    the module's functions.

# 3. The inputInt() function returns an integer, while the inputFloat() function returns a float value.

# 4. Using PyInputPlus, to ensure that the user enters a whole number between 0 and 99 : pyip.inputint(min=0, max=99)

# 5. A list of regular expression strings are transferred to the keyword arguments of allowRegexes and blockRegexes.

# 6. If a blank input is entered three times, inputStr(limit=3)  will raise an RetryLimitException This exception is r

# 7. If blank input is entered three times, inputStr(limit=3, default='hello')  returns the value N/A to the variable
#    username
