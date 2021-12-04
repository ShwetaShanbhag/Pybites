from collections.abc import Iterable
def flatten(l):
    if isinstance(l, Iterable) and not isinstance(l, (str, bytes)):
        for el in l:
            yield from flatten(el)
    else:
        yield l
    