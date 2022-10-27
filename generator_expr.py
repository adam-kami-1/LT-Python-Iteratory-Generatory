import generator_range as gr
import sys


def test(name: str, gen):
    """Display generator type, size and generated values"""
    print(F"\n{name}")
    print("=" * len(name))
    print(F"Object type: {type(gen)}")
    print(F"Object size: {sys.getsizeof(gen)}")
    if isinstance(gen, list):
        print("Getting iterator for list")
        gen = iter(gen)
    # First two generated values taken manually
    print(next(gen))
    print(next(gen))
    # Take the rest in for loop
    for x in gen:
        print(F"<{x}>", end=", ")


def main():
    gen = gr.Frange(0.0, 25.0, 1.0)
    test("Frange class generator", gen)

    gen = (i*2 for i in range(25))
    test("Generator expression", gen)

    gen = [i*2 for i in range(25)]
    test("List comprehension", gen)

    gen = (c+str(no) for c in "abcde" for no in range(5))
    test("Nested generator expression", gen)


if __name__ == "__main__":
    main()
