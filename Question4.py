# Exxample 1-

try:
    a = int("dgd")
    print(a)
except Exception as e:
    print(e)
    print("This is executed")

#Example 2 - 

try:
    a = 5+11
    print(a)
except:
    print("This will not exceuted")
finally:
    print("This will executed as try complete ")

#Example 3 -

class test(Exception):
    "Raise Exception has been Ocured"
    pass

try:
    a = 5
    if a>4:
        raise test
except test:
    print("Custom Exception has been raised")