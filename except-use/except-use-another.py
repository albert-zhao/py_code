# try:
#     x = int(input('enter the first number:'))
#     y = int(input('enter the second number:'))
#     print(x/y)
# except:
#     print('something error happened')
while True:
    try:
        x = int(input('enter the first number:'))
        y = int(input('enter the second number:'))
        print(x/y)
    except Exception as e:
        print('Invalid input:', e)
        print('Please try again')
    else:
        break