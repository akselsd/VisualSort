import random


class Numbers:

    def __init__(self, amount):
        self.numbers = [x for x in range(1, amount+1)]
        random.shuffle(self.numbers)
        self.sorted_numbers = sorted(self.numbers)

    # 1 is correct
    def get_displacement_vector(self):
        n = len(self.sorted_numbers)
        return list(map(lambda x: 1 - abs(self.numbers.index(x) - self.sorted_numbers.index(x)) / (n), self.numbers))

    def reshuffle(self):
        random.shuffle(self.numbers)

    def __bool__(self):
        return self.numbers == self.sorted_numbers