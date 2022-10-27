
def Frange(start: float,
           stop: float = None,  # type: ignore
           step: float = None):  # type: ignore
    """Zwraca generator generujący sekwencję liczb od 'start' (włącznie),
    do (stop) (wyłącznie) co krok wartości: 'step'.

    Typ parametrów i zwracanych wartości jest float.
    Funkcji używa się w jeden z następujących sposobów:
      Frange(stop) - start = 0, step jest 1 lub -1, w zależności od tego
                     czy stop jest większy od 0, czy nie.
      Frange(start, stop[, step]) - domyślną wartością step jest 1 lub -1,
                                    w zależności od tego czy start
                                    jest mniejszy od stop, czy nie.
    Step nie może przyjmować warotści 0.

    Uwaga:
    Oryginalna funkcja range, przyjmuje atrybuty typu int
    i zwraca obiekt typu iterable, a Frange jest generatorem.
    """
    # Przygotowanie parametrów do generatora
    if stop is None:
        start, stop = 0.0, start
    else:
        start, stop = start, stop
    if step is None:
        if start <= stop:
            step = 1.0
        else:
            step = -1.0
    elif step == 0.0:
        raise ValueError("Frange() arg 3 must not be zero")
    else:
        step = step

    # #######################
    # Główna część generatora
    while ((step > 0.0 and start < stop) or (step < 0.0 and start > stop)):
        # print(F"GEN - Yielding {start}")
        ret = yield start
        if ret is not None:
            # print(F"GEN - Received {ret} via .send()")
            start = ret
            continue
        start += step


def test(start: float,
         stop: float = None,  # type: ignore
         step: float = None):  # type: ignore
    li = ", ".join([str(el) for el in Frange(start, stop, step)])
    print(F"Frange({start}, {stop}, {step}) = [{li}]")


def use_number(idx: int, no: float) -> int:
    idx += 1
    print(F"{idx}: {no}")
    return idx


def main():
    print("\nUżycie generatora wewnątrz list comprehension:")
    print("==============================================")
    test(5.0)
    test(0.0, 1.0, 0.1)
    test(8.7, 1.6, -2.3)

    print("\nW następnych przykładach jest użyty generator:")
    print("  Frange(0.0, 1.1, 0.1)")

    print("\nUżycie generatora w instrukcji for:")
    print("===================================")
    idx = -1
    for no in Frange(0.0, 1.1, 0.1):
        idx += 1
        print(F"{idx}: {no}")

    print("\nManualna obsługa generatora:")
    print("============================")
    gen = Frange(0.0, 1.1, 0.1)
    idx = -1
    while True:
        try:
            no = next(gen)
            idx += 1
            print(F"{idx}: {no}")
        except StopIteration:
            break

    print("\nManualne użycie .close() i .send():")
    print("===================================")
    gen = Frange(0.0, 1.1, 0.1)
    idx = -1
    while True:
        try:
            no = next(gen)
            idx = use_number(idx, no)

            if no >= 0.9:
                gen.close()

            # Bardzo "naiwna" próba naprawienia błędów float
            if len(str(no)) > 3:
                no = round(no, 1)
                # print(F"Sending {no} to generator")
                no = gen.send(no)
                # print(F"{no} returned from send({no})")
                idx = use_number(idx, no)

        except StopIteration:
            break

    print("\nUżycie .close() i .send() wewnątrz for:")
    print("=======================================")
    gen = Frange(0.0, 0.8, 0.1)
    idx = -1
    for no in gen:
        idx = use_number(idx, no)

        if no >= 0.9:
            gen.close()

        # Bardzo "naiwna" próba naprawienia błędów float
        if len(str(no)) > 3:
            no = round(no, 1)
            # print(F"Sending {no} to generator")
            try:
                no = gen.send(no)
            except StopIteration:
                break
            # print(F"{no} returned from send({no})")
            idx = use_number(idx, no)


if __name__ == "__main__":
    main()
