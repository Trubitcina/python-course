class fibonacci_sequence:
    def __init__(self, max):
        self.n = 0
        self.a = 1
        self.b = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            a = self.a
            self.n = self.n + 1
            self.a, self.b = self.b, self.a + self.b
            return a
        else:
            raise StopIteration
