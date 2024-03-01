from rich.deriving import deriving_rich_class, deriving_rich
from rich.pretty import is_expandable
from rich import print


@deriving_rich_class
class Foo:
    """
    Hello, world!
    """

    sv1 = 1

    def __init__(self):
        self.cv1 = 1

    def method1(self, a):
        return a


@deriving_rich
class Bar:
    sv1 = 10

    def __init__(self):
        self.cv1 = 1
        self.cv2 = {}
        self.cv3 = "str"


def test_derive_class():
    assert is_expandable(Foo)
    rr = Foo.__rich_class_repr__()
    print(rr)
    assert rr["name"] == "Foo"
    assert rr["doc"] is not None
    assert rr["methods"] == ["method1"]
    assert rr["variables"] == [("sv1", 1)]


def test_derive():
    bar = Bar()
    assert is_expandable(bar)
    rr = bar.__rich_repr__()
    print(rr)
    assert rr["variables"] == {"cv1": 1, "cv2": {}, "cv3": "str"}
