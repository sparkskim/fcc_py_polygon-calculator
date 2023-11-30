class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, value1):
        self.width = value1

    def set_height(self, value2):
        self.height = value2

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            return "Too big for picture."
        else:
            rectangle_shape = []
            for row in range(self.height):
                rectangle_shape.append("*" * self.width + "\n")
            return "".join(rectangle_shape)

    def get_amount_inside(self, shape):
        times_h = 0
        times_w = 0
        while self.width >= shape.width:
            self.width -= shape.width
            times_w += 1
        while self.height >= shape.height:
            self.height -= shape.height
            times_h += 1
        return times_h * times_w

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def set_side(self, value):
        self.width = value
        self.height = value
        self.side = value

    def set_width(self, value):
        self.set_side(value)

    def set_height(self, value):
        self.set_side(value)

    def __str__(self):
        return f"Square(side={self.width})"

    def square_picture(self):
        squre_shape = []
        for row in range(self.height):
            squre_shape.append("*" * self.width + "\n")
        return "".join(squre_shape)
