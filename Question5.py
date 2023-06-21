# Custom Exception is the Exception which use to create the pre-known exception before execution of code.

# Custom Exception is very usefull for our code because it provides the ability to a code that whenever a pre determine Exception has been rasied then customer Exception will make sure that the code exceution would not be stoped.

#Example -

class test(Exception):
    "Raise Exception has been Ocured"
    pass

try:
    a = 5
    if a>4:
        raise test
except test:
    print("Custom Exception has been raised")