# 1. We use the functions to reuse the codes. eg:- Inside function we can write certain lines of codes for any requirement
#    and call that functoin any number of time whenever it is required.

# 2. Codes in a function run when it is called.

# 3. def() statement creates a function.

# 4. function : Defining a function by writing certain lines of codes for a specific requirement or there are pre-defined
#               functions available which can be used by us.
#    function call: Calling the self-defind or pre-defined functions by passing argumrnts if any.

# 5. Global Scope : The scope of global variables are accessible in the entire program
#    Local Scope : The local variables are accessible only inside the functions/methods where it is defined.

# 6. local scope variables after function call returns will be destroyed by gc.

# 7. return statement is used to end the execution of a function and return the result. It is not possible to havea return
#    value to an expression as it is only applicable to function.

# 8. If a function does not have return statement, then return value of that function is 'None'

# 9. To make a function variable refer to global variable by using the key word global.
#    eg:-   class Demo:
#               def test(self):
#                   global a
#                   a = 10
#           print(a)

# 10. In python None is a data type, type of None is NoneType itself.

# 11. "import areallyourpetsnamederic" statement imports a module named areallyourpetsnamederic.

# 12. If I am having a bacon() feature in a spam module, after importing spam I'll call it like :- spam.bacon()

# 13. To save a programme from crashing if it encounters an error we can use try & except clause.

# 14. In try clause we keep the risky codes which has a chance to raise error.
#     In except clause we keep the corresponding exception class, and alternate code to handle it.