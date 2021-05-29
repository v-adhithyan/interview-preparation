from enum import Enum


class Size(Enum):
    SMALL = 0
    LARGE = 1


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


class Product:

    def __init__(self, size, color):
        self.size = size
        self.color = color


class Specification:

    def is_satisfied(self, item):
        pass


class Filter:

    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):

    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):

    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):

    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(), self.args
        ))


class BetterFilter(Filter):

    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied():
                yield item


if __name__ == '__main__':
    pass
