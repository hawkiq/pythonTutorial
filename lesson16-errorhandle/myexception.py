n1 = 10
n2 = 0
try:
    r = n1 / n2
    print(r)
except TypeError as e:
    print("You divided by string try again")
except ZeroDivisionError as e:
    print("You divided by Zero ")
except Exception as e:
    print(type(e).__name__)

