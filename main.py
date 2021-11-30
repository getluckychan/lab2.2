import copy


class Complex(object):
    def __init__(self, x):
        self.x = complex(x)

    def __add__(self, other):
        return self.x - other.x

    def __sub__(self, other):
        return self.x - other.x

    def __iadd__(self, other):
        self.x = self + other
        return self.x

    def __isub__(self, other):
        self.x = self - other
        return self.x

    def __mul__(self, other):
        return self.x * other.x

    def __truediv__(self, other):
        return self.x / other.x

    def __imul__(self, other):
        self.x = self * other
        return self.x

    def __itruediv__(self, other):
        self.x = self / other
        return self.x

    @classmethod
    def from_foo(cls, class_instance):
        x = copy.deepcopy(class_instance.x)
        return cls(x)
