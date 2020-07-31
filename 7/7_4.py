#!/bin/python


def counter():
    counter = 0

    def _increment():
        nonlocal counter
        counter += 1
        return counter
    return _increment


if __name__ == "__main__":
    counter1 = counter()
    counter2 = counter()
    for x in range(5):
        print(f'{counter1()=}, {counter2()=}')
