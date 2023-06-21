# 1. Exception in python helps the code to handle the unwanted error and also instead of getting error Exception helps that program to excecuted.
# 2. Syntax errors produce the errors and program would not be exceuted properly but while excetion we can handle the errors and also can execute the program.

#Example - 

try:
    a = 10/0
except Exception as e:
    print(e)
