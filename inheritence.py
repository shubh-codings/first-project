class Fibonacci():

    def __init__(self, n):
        self.n = n

    def fib_max(self):  # for series upto a maximum number limit
        print('Fibonacci series is : ')
        total = 0
        limit = self.n

        a = 0
        b = 1
        if self.n > 0:
            print(a)
            print(b)

            while total < limit:
                c = a + b
                a = b
                b = c
                print(c)
                total = total + a

        else:
            print(a)

    def fib(self):

        a = 0
        b = 1

        if self.n > 1:

            print(a)
            print(b)

        else:
            print(a)

        for i in range(2, self.n):
            c = a + b
            a = b
            b = c
            print(c)


pos = -1


class Search():
    def __init__(self, list, y):
        self.list = list
        self.y = y

    def bin_search(self):  # for binary search method
        l = 0
        u = len(self.list) + 1

        for i in range(u + 1):

            mid = (l + u) // 2

            if self.list[mid] == self.y:
                globals()['pos'] = mid
                return True
            elif self.list[mid] < self.y:
                l = mid

            else:
                u = mid
        return False

    def search(self):  # For Linear search method

        for i in range(len(self.list)):
            if self.list[i] == self.y:
                globals()['pos'] = i
                return True
        return False


class Combine(Fibonacci, Search):

    def __init__(self, list, y, n):
        Fibonacci.__init__(self, n)
        Search.__init__(self, list, y)



try:

    list = [7, 8, 5, 14, 9, 15, 22, 35, 12, 20, 19, 33]
    list.sort()
    print(list)
    y = int(input('Please enter the number : '))
    a1 = Combine(list, y, y)
    # using binary search
    if a1.bin_search():
        print('found the number at ', pos + 1)
    else:
        print('number not found')

    # using linear search
    if a1.search():
        print('found the number at ', pos + 1)
    else:
        print('number not found')
    a1.fib_max()
except Exception as e:
    print(e)
