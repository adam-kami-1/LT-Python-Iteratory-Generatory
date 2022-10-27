from iterators import test


# Wariant 1
# =========
# Domyślny iterator używa metod: __len()__ i __getitem()__.
# Pokazuje wszystkie (również puste == None) elementy listy.

# Wariant 2
# =========
# Wykorzystuje iterator enumerate i iterator listy self._data.
# Pokazuje wszystkie (również puste == None) elementy listy w
# postaci krotki zawierającej indeks i wartość elementu.
# Stanowi bazę dla docelowego iteratora z wariantu 3.

# Wariant 3
# =========
# Iterator odfiltrowuje niepuste elementy i zwraca niepuste elementy
# listy w postaci krotki zawierającej indeks i wartość elementu.

VARIANT = 1


if VARIANT > 1:
    class SparseListL_iterator:

        def __init__(self, obj):
            self._obj = obj
            if VARIANT == 2:
                self._iter = iter(enumerate(self._obj._data))
            else:
                self._iter = -1

        def __iter__(self):
            if VARIANT == 2:
                self._iter = iter(enumerate(self._obj._data))
            else:
                self._iter = -1
            return self

        if VARIANT == 2:

            def __next__(self):
                return next(self._iter)

        if VARIANT == 3:

            def __next__(self):
                while self._iter + 1 < len(self._obj._data):
                    self._iter += 1
                    if self._obj._data[self._iter] is not None:
                        return self._iter, self._obj._data[self._iter]
                raise StopIteration


class SparseListL:
    """Klasa implementująca rzadką macierz 1-wymiarową (listę).

    Większość elementów listy jest pusta (==None). Klasa pozwala na
    tworzenie pustej listy o zadanym wymiarze. Można dodawać i ustawiać
    dowolny element listy (lista jest ewentualnie wydłużana).
    Brak obsługi ustawiania wartości None, t.j. usuwania elementu,
    jak również możliwości skracania listy.
    Standardowa funkcja len() zwraca ilość wszystkich elementów.

    Domyślny iterator ma zwracać tylko niepuste elementy w kolejności
    rosnących indeksów, jako krotka zawierająca indeks i wartość elementu.

    Implementacja SparseListL jest oparta na wykorzystaniu listy
    zawierającej wszystkie, również puste (== None) elementy rzadkiej
    macierzy.
    """

    def __init__(self, data_len: int = 0):
        self._data = [None for _ in range(data_len)]

    def __len__(self):
        # print("Called SparseListL.__len__()")
        return len(self._data)

    def __getitem__(self, key: int):
        # print(F"Called SparseListL.__getitem__({key})")
        return self._data[key]

    def __setitem__(self, key: int, value):
        if len(self._data) < key:
            for _ in range(len(self._data), key):
                self._data.append(None)
            self._data.append(value)
            return
        self._data[key] = value

    def __repr__(self):
        if VARIANT < 3:
            return ("SparseListL("
                    + ", ".join([str(i) + ":" + repr(v)
                                for i, v in enumerate(self._data)
                                if v is not None])
                    + ")")
        else:
            return ("SparseListL("
                    + ", ".join([str(i) + ":" + repr(v)
                                for i, v in iter(self)])
                    + ")")

    if VARIANT > 1:
        def __iter__(self):
            return SparseListL_iterator(self)


def main():
    test(SparseListL)


if __name__ == "__main__":
    main()
