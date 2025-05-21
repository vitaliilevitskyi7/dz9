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

    def __copy__(self):
        return Rational(self._n, self._d)

    def __str__(self):
        return f"{self._n}/{self._d}"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        other = Rational(other) if isinstance(other, int) else other
        return Rational(self._n * other._d + other._n * self._d, self._d * other._d)

    def __sub__(self, other):
        other = Rational(other) if isinstance(other, int) else other
        return Rational(self._n * other._d - other._n * self._d, self._d * other._d)

    def __mul__(self, other):
        other = Rational(other) if isinstance(other, int) else other
        return Rational(self._n * other._n, self._d * other._d)

    def __truediv__(self, other):
        other = Rational(other) if isinstance(other, int) else other
        if other._n == 0:
            raise ZeroDivisionError("Division by zero")
        return Rational(self._n * other._d, self._d * other._n)

    def __call__(self):
        return self._n / self._d

    def __getitem__(self, key):
        if key == "n":
            return self._n
        if key == "d":
            return self._d
        raise KeyError("Use 'n' for numerator or 'd' for denominator")

    def __setitem__(self, key, value):
        if key == "n":
            self._n = value
        elif key == "d":
            if value == 0:
                raise ValueError("Denominator cannot be zero")
            self._d = value
        else:
            raise KeyError("Use 'n' for numerator or 'd' for denominator")
        g = gcd(self._n, self._d)
        self._n //= g
        self._d //= g
        if self._d < 0:
            self._n *= -1
            self._d *= -1


def evaluate_expression(expr: str) -> Rational:
    tokens = expr.strip().split()
    result = None
    current_op = '+'

    def parse_token(tok):
        return Rational(tok) if '/' in tok else Rational(int(tok))

    for tok in tokens:
        if tok in '+-*/':
            current_op = tok
        else:
            val = parse_token(tok)
            if result is None:
                result = val
            else:
                if current_op == '+':
                    result = result + val
                elif current_op == '-':
                    result = result - val
                elif current_op == '*':
                    result = result * val
                elif current_op == '/':
                    result = result / val
    return result


def main():
    with open("input01.txt", "r") as fin, open("output_demo.txt", "w") as fout:
        for line in fin:
            try:
                res = evaluate_expression(line)
                fout.write(f"{line.strip()} = {res} = {res():.5f}\n")
            except Exception as e:
                fout.write(f"{line.strip()} = Error: {e}\n")

if __name__ == "__main__":
    main()
