# This cell contains some utility functions to prepare and execute the benchmarks
import timeit
from statistics import median
from random import choice
from string import ascii_uppercase


def random_string(length):
    """Produce a random string made of *length* uppercase ascii characters"""
    return ''.join(choice(ascii_uppercase) for i in range(length))


def print_scaling(stmt, setup, sizes=None, repeat=False, units='us'):
    """Print scaling information for the statement *stmt*, executed after *setup*.

    The *setup* and *stmt* arguments take a template string where "{N}"
    will be replaced as the size of the input.

    The *repeat* flags determined if the setup needs to be run between
    each test run.
    """
    if not sizes:
        sizes = [10000, 20000, 30000]
    values = []
    for size in sizes:
        if repeat:
            timings = timeit.repeat(stmt.format(N=size),
                                    setup=setup.format(N=size),
                                    number=1, repeat=1000)
            values.append(min(timings))
        else:
            timings = timeit.repeat(stmt.format(N=size),
                                    setup=setup.format(N=size),
                                    number=1000, repeat=3)
            values.append(min(t / 1000 for t in timings))
    unit_factor = {'us': 1e6,
                   'ms': 1e3}[units]

    print(' | '.join('N = {} t = {:.2f} ({})'.format(n, t * unit_factor, units) for n, t in zip(sizes, values)))


if __name__ == "__main__":
    pass
