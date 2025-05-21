from math import gcd
from typing import Union

class Rational:
    def __init__(self, n: Union[int, str], d: int = 1):
        if isinstance(n, str):
            n, d = map(int, n.split("/"))
        if d == 0:
            raise ValueError("Denominator cannot be zero")
        g = gcd(n, d)
        self._n = n // g
        self._d = d // g
        if self._d < 0:
            self._n *= -1
            self._d *= -1

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self._n * other._d + other._n * self._d, self._d * other._d)

    def __str__(self):
        return f"{self._n}/{self._d}"

    def __call__(self):
        return self._n / self._d

class RationalList:
    def __init__(self):
        self.items = []

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        if isinstance(value, int):
            value = Rational(value)
        if not isinstance(value, Rational):
            raise TypeError("Only Rational or int allowed")
        self.items[index] = value

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        new_list = RationalList()
        new_list.items = self.items.copy()
        if isinstance(other, RationalList):
            new_list.items += other.items
        else:
            new_list.items.append(Rational(other) if isinstance(other, int) else other)
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.items += other.items
        else:
            self.items.append(Rational(other) if isinstance(other, int) else other)
        return self

    def append(self, value):
        if isinstance(value, int):
            value = Rational(value)
        if not isinstance(value, Rational):
            raise TypeError("Only Rational or int allowed")
        self.items.append(value)

    def sum(self):
        result = Rational(0)
        for item in self.items:
            result += item
        return result


def read_file_to_rationallist(filepath):
    rlist = RationalList()
    with open(filepath, 'r') as f:
        for line in f:
            tokens = line.strip().split()
            for tok in tokens:
                rlist.append(Rational(tok) if '/' in tok else Rational(int(tok)))
    return rlist


def main():
    files = ["input01 (1).txt", "input02.txt", "input03.txt"]
    with open("output_demo2.txt", "w") as out:
        for fname in files:
            try:
                rlist = read_file_to_rationallist(fname)
                s = rlist.sum()
                out.write(f"{fname}: {s} = {s():.5f}\n")
            except Exception as e:
                out.write(f"{fname}: Error - {str(e)}\n")

if __name__ == "__main__":
    main()
