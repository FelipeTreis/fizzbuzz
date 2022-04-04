"""
Rules of Fizzbuzz

1. If the position is multiple of 3: fizz
2. If the position is multiple of 5: buzz
3. If the position is multiple of 3 and 5: fizzbuzz
4. For any other position speak the own number.
"""
from functools import partial


multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def robot(pos):
    speak = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
        speak = 'fizzbuzz'
    elif multiple_of_5(pos):
        speak = 'buzz'
    elif multiple_of_3(pos):
        speak = 'fizz'

    return speak


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'