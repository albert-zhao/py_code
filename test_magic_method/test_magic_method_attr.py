class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        print('now in __setattr__')
        if name == 'size':
            self.width, self.height = value
        else:
            print('now in __setattr__ else')
            self.__dict__[name] = value


if __name__ == '__main__':
    r = Rectangle()
    # r.size = (3, 5)
    # print(r.size)
    # r.width = 3
    # print(r.width)
    # print(r.__dict__)