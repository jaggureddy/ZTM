"""
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints
Use try/except to catch exceptions.

"""

def divide(n,d):
    try:
        c = n/d
    except ZeroDivisionError:
        print("divide by zero exception")
    except Exception:
        print("Exception captured")


divide(5,0)