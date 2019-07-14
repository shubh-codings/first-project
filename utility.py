class Utility:
    def __init__(self, n):
        self.n = n

    def find_max(self):
        maximum = self.n[0]
        for number in self.n:
            if number > maximum:
                maximum = number
        return maximum
