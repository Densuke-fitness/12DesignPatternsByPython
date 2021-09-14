class Rectangle:

  def __init__(self, width, height) -> None:
      self.width = width
      self.height = height
  
  def calcurate_area(self):
    return self.width * self.height


class Square(Rectangle):

  def __init__(self, size) -> None:
      self.height = self.width = size

def print_area(obj):
  print(obj.calcurate_area())

r = Rectangle(10,2)
s = Square(5)

print_area(r)
print_area(s)