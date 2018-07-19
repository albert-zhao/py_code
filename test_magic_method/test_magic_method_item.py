def check_index(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmaticSeqence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __len__(self):
        return 10

    def __getitem__(self, key):
        print('now in  __getitem__')
        check_index(key)
        try:
            print('now in  __getitem__ -> try')
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        print('now in __setitem__ before check_index')
        check_index(key)
        print('now in __setitem__ after check_index')
        self.changed[key] = value


if __name__ == '__main__':
    s = ArithmaticSeqence()
    s[4] = 2
    print(s[4])
    print(s[5])
    print(len(s))
    # del s[4]
    # s['hello'] = 3
    # s[-1]
