import typing
from fractions import Fraction
from decimal import Decimal


Number = typing.TypeVar("Number", int, float, Fraction, Decimal)
# Number = [int, float, Fraction, Decimal]


class Frange:
    """Zwraca iterator generujący sekwencję liczb od 'start' (włącznie),
    do (stop) (wyłącznie) co krok wartości: 'step'.

    Typ zwracanych wartości jest identyczny z typem pierwszego argumentu,
    i może być int, float, Fraction lub Decimal.
    Klasy używa się w jeden z następujących sposobów:
      Frange(stop) - start = 0, step jest 1 lub -1, w zależności od tego
                     czy stop jest większy od 0, czy nie.
      Frange(start, stop[, step]) - domyślną wartością step jest 1 lub -1,
                                    w zależności od tego czy start
                                    jest mniejszy od stop, czy nie.
    Step nie może przyjmować warotści 0.

    Uwaga:
    Oryginalna funkcja range, przyjmuje atrybuty tylko typu int
    i zwraca obiekt typu iterable, a Frange zwraca iterator.
    """

    def __init__(self,
                 start: Number,
                 stop: Number = None,
                 step: Number = None):
        # Zapamiętaj typ pierwszego argumentu
        self._type = type(start)
        # Ustaw start i stop
        if stop is None:
            self._start, self._stop = self._type(0), start
        else:
            self._start, self._stop = start, self._type(stop)  # type: ignore
        # Ustaw step
        if step is None:
            if self._start <= self._stop:
                self._step = self._type(1)
            else:
                self._step = self._type(-1)
        elif step == self._type(0):
            raise ValueError("Frange() arg 3 must not be zero")
        else:
            self._step = self._type(step)  # type: ignore
        # Ustaw wartość bieżącą zwracaną przez next()
        self._element = self._start - self._step

    def __iter__(self):
        # Ustaw wartość bieżącą zwracaną przez next()
        self._element = self._start - self._step
        return self

    def __next__(self):
        self._element += self._step
        if ((self._step > self._type(0) and self._element >= self._stop)
           or (self._step <= self._type(0) and self._element <= self._stop)):
            raise StopIteration
        return self._element


def test(start: Number,
         stop: Number = None,
         step: Number = None):
    li = ", ".join([str(el) for el in Frange(start, stop, step)])
    print(F"Frange({start}, {stop}, {step}) = [{li}]")


if __name__ == "__main__":
    print("\nFloat")
    print("=====")
    test(5.0)
    test(0.0, 1.0, 0.1)
    test(8.7, 1.6, -2.3)
    print("\nDecimal")
    print("=======")
    test(Decimal("5.0"))
    test(Decimal("0.0"), Decimal("1.0"), Decimal("0.1"))
    test(Decimal("8.7"), Decimal("1.6"), Decimal("-2.3"))
    print("\nFraction")
    print("========")
    test(Fraction(5))
    test(Fraction(0, 10), Fraction(10, 10), Fraction(1, 10))
    test(Fraction(87, 10), Fraction(16, 10), Fraction(-23, 10))
