pos = -1

'''
def search(lis, x):

    i = 0
    while i < len(lis):
        if lis[i] == x:
            globals()['pos'] = i
            return True
        i = i + 1
    return False
'''


class Search:
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


list = [7, 8, 5, 14, 9, 15, 22, 35, 12, 20, 19, 33]
list.sort()
print(list)
y = int(input('Please enter thenumber you want to search : '))
a1 = Search(list, y)
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
