from iterators import test


# Wariant 1
# =========
# Domyślny iterator używa metod: __len()__ i __getitem()__.
# Pokazuje wszystkie (również puste == None) elementy listy.

# Wariant 2
# =========
# Wykorzystuje iterator słownika self._data.
# Pokazuje tylko niepuste elementy listy.
#
# Pokazuje je uprządkowane tak jak dict, czyli w kolejności dodawania
# elementów do słownika!!!!!!
# Poprawienie tego wymaga zakodowania jednego z rozwiązan, zależnych
# od spodziewanej charakterystyki użycia, np: maksymalny rozmiar całej
# tablicy, spodziewana ilość niepustych elementów, częstotliwość
# dodawania elementów, itp.

# Wariant 3
# =========
# Wariant ten zakłada, że niepustych elementów jest bardzo mało
# i są rzadko dodawane. A więc po serii dodawań elementów, możemy
# przesortować trzymane osobno indeksy niepustych elementów.

VARIANT = 1


if VARIANT == 2:
    class SparseListD_iterator:

        def __init__(self, obj):
            self._obj = obj
            self._iter = iter(self._obj._data.items())

        def __iter__(self):
            self._iter = iter(self._obj._data.items())
            return self

        def __next__(self):
            return next(self._iter)


if VARIANT == 3:
    class SparseListD_iterator:

        def __init__(self, obj):
            self._obj = obj
            self._iter = iter(self._obj._key_list)

        def __iter__(self):
            self._iter = iter(self._obj._key_list)
            return self

        def __next__(self):
            key = next(self._iter)
            return key, self._obj._data[key]


class SparseListD:
    """Klasa implementująca rzadką macierz 1-wymiarową (listę).

    Większość elementów listy jest pusta (==None). Klasa pozwala na
    tworzenie pustej listy o zadanym wymiarze. Można dodawać i ustawiać
    dowolny element listy (lista jest ewentualnie wydłużana).
    Brak obsługi ustawiania wartości None, t.j. usuwania elementu,
    jak również możliwości skracania listy.
    Standardowa funkcja len() zwraca ilość wszystkich elementów.

    Domyślny iterator ma zwracać tylko niepuste elementy w kolejności
    rozsnących indeksów, jako krotka zawierająca indeks i wartość elementu.

    Implementacja SparseListD jest oparta na wykorzystaniu słownika
    zawierającego tylko niepuste (!= None) elementy rzadkiej macierzy.
    """

    def __init__(self, data_len: int = 0):
        self._iter = None
        self._data = {}
        self._data_len = data_len
        if VARIANT == 3:
            self._key_list = []
            self._sorted = True

    def __len__(self) -> int:
        # print("Called SparseListD.__len__()")
        return self._data_len

    def __getitem__(self, key: int):
        # print(F"Called SparseListD.__getitem__({key})")
        if key in self._data:
            return self._data[key]
        elif key < self._data_len:
            return None
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, key: int, value):
        self._data_len = max(self._data_len, key + 1)
        self._data[key] = value
        if VARIANT == 3:
            self._key_list.append(key)
            self._sorted = False

    def __repr__(self) -> str:
        if VARIANT == 1:
            return ("SparseListL("
                    + ", ".join([str(i) + ":" + repr(v)
                                for i, v in self._data.items()])
                    + ")")
        else:
            return ("SparseListL("
                    + ", ".join([str(i) + ":" + repr(v)
                                for i, v in iter(self)])
                    + ")")

    if VARIANT > 1:
        def __iter__(self):
            if VARIANT == 3:
                if not self._sorted:
                    self._key_list.sort()
                    self._sorted = False
            return SparseListD_iterator(self)


def main():
    test(SparseListD)


if __name__ == "__main__":
    main()
