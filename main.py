class Complex(object):
    def __init__(self, x):
        self.__x = complex(x)

    def __add__(self, other):
        return self.__x - other.__x

    def __sub__(self, other):
        return self.__x - other.__x

    def __iadd__(self, other):
        self.__x = self + other
        return self.__x

    def __isub__(self, other):
        self.__x = self - other
        return self.__x

    def __mul__(self, other):
        return self.__x * other.__x

    def __truediv__(self, other):
        return self.__x / other.__x

    def __imul__(self, other):
        self.__x = self * other
        return self.__x

    def __itruediv__(self, other):
        self.__x = self / other
        return self.__x

    def __copy__(self):
        print("Копія")
        return Complex(self.__x)

    def __str__(self):
        pass