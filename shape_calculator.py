class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        width = self.width
        return width

    def set_hegith(self, height):
        height = self.height
        return height

    def get_area(self, area):
        area = self.width * self.height
        return area

    def get_perimeter(self, perimeter):
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

    def get_diagonal(self, diagonal):
        diagonal = (self.width**2 + self.height**2) ** 0.5
        return diagonal

    def get_picture(self):
        width = self.width
        height = self.height

        print_width = "*" * width + "\n" * height
        print_height = "*" * height + " " * width
        return print_width, print_height

    def get_amount_inside(another_shape, width, height):
        rectangle_string = f"Rectangle(width = {width}, height = {height})"
        return rectangle_string

    class Square:
        def __init__(self, width, height):
            side_length = self.width
            side_length = self.h

        def set_side(side):
            side_string = f"Square(side={side})"
            return side_string
