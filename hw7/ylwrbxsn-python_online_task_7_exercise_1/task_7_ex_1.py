"""
Develop Rectangle class with following content:
    2 private fields type of float `side_a` and `side_b` (sides А and В of the rectangle);
    One constructor with two optional parameters a and b (parameters specify rectangle sides). Side А of a rectangle
    defaults to 4, side В - 3. Raise ValueError if received parameters are less than or equal to 0;
    Method `get_side_a`, returning value of the side А;
    Method `get_side_b`, returning value of the side В;
    Method `area`, calculating and returning the area value;
    Method `perimeter`, calculating and returning the perimeter value;
    Method `is_square`, checking whether current rectangle is square or not. Returns True if the shape is square and
    False in another case;
    Method `replace_sides`, swapping rectangle sides.

Develop class ArrayRectangles, in which declare:
    Private attribute `rectangle_array` (list of rectangles);
    One constructor that creates a list of rectangles with length `n` filled with `None` and that receives an
    arbitrary amount of objects of type `Rectangle` or a list of objects of type `Rectangle` (the list must be
    unpacked inside the constructor so that there will be no nested arrays). If both objects and length are passed,
    at first creates a list with received objects and then add the required number of Nones to achieve the
    desired length. If `n` is less than the number of received objects, the length of the list will be equal to the
    number of objects;
    Method `add_rectangle` that adds a rectangle of type `Rectangle` to the array on the nearest free place and
    returning True, or returning False, if there is no free space in the array;
    Method `number_max_area`, that returns order number (index) of the first rectangle with the maximum area value
    (numeration starts from zero);
    Method `number_min_perimeter`, that returns order number (index) of the first rectangle with the minimum area value
    (numeration starts from zero);
    Method `number_square`, that returns the number of squares in the array of rectangles
"""


class Rectangle:
    def __init__(self, a: float = 4.0, b: float = 3.0):
        if a <= 0 or b <= 0:
            raise ValueError
        self.__side_a = a
        self.__side_b = b

    def get_side_a(self) -> float:
        return self.__side_a

    def get_side_b(self) -> float:
        return self.__side_b

    def area(self) -> float:
        return self.__side_a * self.__side_b

    def perimeter(self) -> float:
        return 2 * (self.__side_a + self.__side_b)

    def is_square(self) -> bool:
        return self.__side_a == self.__side_b

    def replace_sides(self):
        self.__side_a, self.__side_b = self.__side_b, self.__side_a


class ArrayRectangles:
    def __init__(self, *args, n=0):
        self.__rectangle_array = []
        if args:
            for arg in args:
                if isinstance(arg, Rectangle):
                    self.__rectangle_array.append(arg)
                elif isinstance(arg, (list, tuple)):
                    self.__rectangle_array.extend(arg)
                else:
                    raise ValueError
        if len(self.__rectangle_array) < n:
            self.__rectangle_array += (n - len(self.__rectangle_array)) * [None]

    def add_rectangle(self, rectangle) -> bool:
        try:
            x = self.__rectangle_array
            x[x.index(None)] = rectangle
            return True
        except ValueError:
            return False

    def number_max_area(self) -> int:
        max_area_rect = self.__rectangle_array[0].area()
        lis = []
        for i in self.__rectangle_array:
            if isinstance(i, Rectangle) and (x := float(i.area())) > max_area_rect:
                 max_area_rect = x
                 lis.append(x)
            else:
                lis.append(x)
        return lis.index(max_area_rect)

    def number_min_perimeter(self) -> int:
        min_area_perimeter = self.__rectangle_array[0].perimeter()
        lis = []
        for i in self.__rectangle_array:
            if isinstance(i, Rectangle) and (x := i.perimeter()) < min_area_perimeter:
                min_area_perimeter = x
                lis.append(x)
            else:
                lis.append(x)
        return lis.index(min_area_perimeter)

    def number_square(self) -> int:
        return sum(1 for x in self.__rectangle_array if isinstance(x, Rectangle) and x.is_square())



mysquare = Rectangle(15,20)

print(mysquare.get_side_a())
print(mysquare.get_side_b())
print(mysquare.area())
list_of_rectangles = [Rectangle(10, 10), Rectangle(15, 21),
                      Rectangle(16, 20), Rectangle(15, 22),
                      Rectangle(17, 20), Rectangle(15, 23),
                      Rectangle(18, 20), Rectangle(30, 30)]
mylist = ArrayRectangles(list_of_rectangles, Rectangle(50, 200), n=10)
print(mylist.number_square())
print(mylist.number_max_area())
print(mylist.number_min_perimeter())
print(mylist._ArrayRectangles__rectangle_array)