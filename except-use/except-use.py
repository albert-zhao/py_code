try:
    x = int(input('enter the first number:'))
    y = int(input('enter the second number:'))
    print(x/y)
except (ZeroDivisionError, TypeError) as e:
    print(e)
