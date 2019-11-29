import weakref


class Shape:
    all_shapes = []
    def __init__(self, *args, **kwargs):
        self.all_shapes.append(weakref.ref(self))

    @classmethod
    def count(cls):
        for wref in cls.all_shapes:
            shape = wref()
            if shape:
                yield shape


class Line(Shape):
    def __init__(self, length):
        super().__init__(length)
        self.length = length

class Square(Line):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        print(self.length * self.length)

    def perimeter(self):
        return 4 * self.length

class Cube(Square):
    def __init__(self, length):
        super().__init__(length)

    def volume(self):
        return self.length * self.length * self.length

class Rectangle(Line):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def __repr__(self):
        return f'Length : {self.length} Width : {self.width}.'

    def __str__(self):
        return f'Length : {self.length()} Width : {self.width()} Area : {self.area()} Perimeter : {self.perimeter()}'


    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Box(Rectangle):
    def __init__(self, length, width, depth):
        self.depth = depth
        super().__init__(length, width)

    def volume(self):
        return self.length * self.width * self.depth


if __name__ == '__main__':
    l = Line(9)
    s = Square(6)
    r = Rectangle(3, 6)
    b = Box(3, 6, 9)

    print(l.__dict__)
    print(s.__dict__)
    print(r.__dict__)
    print('Box: ' + str(b.__dict__))
    print('Shape: ' + str(Shape.__dict__))
    print('Box Class: ' + str(Box.__dict__.keys()))
    print('Box Class Dir: ' + str(dir(Box.__dict__)))
    print(Line.__dict__)
    print(Box.__dict__)
    print(Box.__name__)
