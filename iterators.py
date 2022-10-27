def isiterable(obj: object) -> bool:
    """Verity if input object is an iterable.

    Args:
        obj: Input object to verify

    Returns:
        True - if object has attribute __iter__ or
               object has attributes __len__ and __getitem__.
               There is missing verification if key parameter
               of __get_item__ is int.
        False - in other cases.
    """
    if hasattr(obj, "__iter__"):
        # print("Object has attribute __iter__")
        return True
    if hasattr(obj, "__len__") and hasattr(obj, "__getitem__"):
        # print("Object has attributes __len__ and __getitem__")
        return True
    # print("Object is not iterable")
    return False


def isiterator(obj: object) -> bool:
    """Verity if input object is an iterator.

    Args:
        obj: Input object to verify

    Returns:
        True - if object has attribute __next__.
        False - in other cases.
    """
    if hasattr(obj, "__next__"):
        # print("Object has attribute __next__")
        return True
    # print("Object is not iterator")
    return False


def check_iterable(obj: object) -> None:
    """Display if input object is iterable and/or iterator.

    Args:
        obj: Input object to verify
    """
    print("Object of type "
          F"{type(obj).__qualname__} is "
          F"{'' if isiterable(obj) else 'not '}iterable "
          F"and {'' if isiterator(obj) else 'not '}iterator.")


def check_object(obj: object) -> None:
    """Check if object is iterable and you can get iterator for it.

    If you can get iterator, use it to retreive first item and didplay it.

    Args:
        obj: Input object to verify
    """
    print()
    check_iterable(obj)
    try:
        itr = iter(obj)  # type: ignore
        check_iterable(itr)
        print(repr(next(itr)))
    except TypeError as e:
        print("TypeError:", e)


def basic_tests() -> None:
    """Some basic test for various iterables and iterators.
    """
    check_object(list(range(10)))
    check_object(set(range(10)))
    check_object(range(10))
    check_object("0123456789")
    check_object({0: "0", 1: "1", 2: "2", 3: "3"})
    check_object(10)

    lista = list(range(10))

    print("\n\nRegular instruction for element in iterable.")
    for element in lista:
        print(element, end=", ")

    print("\n\nRegular instruction for element in iterator.")
    for element in iter(lista):
        print(element, end=", ")

    print("\n\nManual iterator usage.")
    iterator = iter(lista)
    while True:
        try:
            element = next(iterator)
        except StopIteration:
            break
        print(element, end=", ")

    print("\n\nManual iterator usage, again.")
    iterator = iter(lista)  # If you comment this line nothing will be printed.
    while True:
        try:
            element = next(iterator)
        except StopIteration:
            break
        print(element, end=", ")


def test(typ) -> None:
    """Test sparse list implementations.

    It is imported in modules implementing sparse list.

    Args:
        typ: class implementing sparse list to be tested.
    """
    matrix = typ(12)
    matrix[3] = "3"  # random.randint(1, 10)
    matrix[9] = "9"  # random.randint(1, 10)
    matrix[5] = "5"  # random.randint(1, 10)

    print(F"\ntest({typ.__qualname__})")
    print("=================")
    check_object(matrix)

    print("\nDisplay matrix using: __repr__():")
    print(matrix)
    print("len(matrix) =", len(matrix))

    print("\nDisplay matrix using: for i in range(len(matrix)):")
    for i in range(len(matrix)):
        print(str(i) + ":" + repr(matrix[i]))

    print("\nDisplay matrix using: for i in matrix:")
    for i in matrix:
        print(repr(i))

    print("\nDisplay matrix using iterator manualy:")
    print("matrix type:", type(matrix).__qualname__)
    itr = iter(matrix)
    print("itr type:", type(itr).__qualname__)
    while True:
        try:
            v = next(itr)
            print(repr(v))
        except StopIteration:
            break


def main():
    basic_tests()


if __name__ == "__main__":
    main()
