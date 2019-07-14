class Fibonacci:

    def __init__(self, n):
        self.n = n

    def fib_max(self):  # for series upto a maximum number limit

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


x = int(input('please enter the no of Fibonacci terms : '))

fib1 = Fibonacci(x)
fib1.fib()

# y =int(input('Please enter the max limit : '))
# fib2 = Fibonacci(y)
# fib2.fib_max()
