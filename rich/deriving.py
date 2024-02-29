from inspect import isclass, ismethod, getmembers, isfunction
from typing import List, Tuple, Any


def deriving_rich_class(c: type) -> type:
    """
    Generate `__rich_class_repr__` method for any class.

    Nothing will be changed if the method already exists.
    """
    assert isclass(c)
    members: List[Tuple[str, Any]] = getmembers(c)
    if "__rich_class_repr__" in map(lambda x: x[0], members):
        return c
    public = list(filter(lambda x: not x[0].startswith("__"), members))
    methods = filter(lambda x: isfunction(x[1]), public)
    variables = filter(lambda x: not isfunction(x[1]), public)
    c.__rich_class_repr__ = lambda: {
        "type": "class",
        "name": c.__name__,
        "doc": c.__doc__,
        "methods": list(map(lambda x: x[0], methods)),
        "variables": list(variables),
    }
    return c


def deriving_rich(c: type) -> type:
    """
    Generate `__rich_repr__` method for any class.

    Nothing will be changed if the method already exists.
    """
    assert isclass(c)
    if "__rich_repr__" in dir(c):
        return c
    c.__rich_repr__ = lambda self: {
        "instance": self.__class__.__name__,
        "variables": self.__dict__,
    }
    return c
