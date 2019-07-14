class Sort:
    def __init__(self, lst):
        self.li = lst

    def bubble_sort(self):
        u = len(self.li)
        for i in range(u - 1, 0, -1):
            for j in range(i):
                if self.li[j] > self.li[j + 1]:
                    temp = self.li[j + 1]
                    self.li[j + 1] = self.li[j]
                    self.li[j] = temp

                # print(li)

    def selection_sort(self):
        u = len(self.li)
        for i in range(u-1):
            min_pos = i
            for j in range(i, u-1):
                if self.li[j] < self.li[min_pos]:
                    min_pos = j

            temp = li[i]
            li[i] = li[min_pos]
            li[min_pos] = temp

            print('selection sorting....', li)


try:

    li = [56, 89, 25, 22, 8, 75, 46, 33, 15, 100]
    print('before sorting', li)

    s2 = Sort(li)
    s2.selection_sort()
    print('after selection sort ', li)

except Exception as e:
    print(e)
