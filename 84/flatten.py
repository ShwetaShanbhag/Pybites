from collections.abc import Iterable
def flatten(list_of_lists):

    for l in list_of_lists:
        if isinstance(l, Iterable) and not isinstance(l, (str, bytes)):
            yield from flatten(l)
        else:
            yield l
    