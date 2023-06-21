# Customer Exception Class with Example 

class example_class(Exception):
    "Raised only when the Exception Occured."
    pass

#Program Starts---
try:
    a = 5
    if a >4:
        raise example_class
except:
    print("Custom Exception has been Occured because a is greater 4")