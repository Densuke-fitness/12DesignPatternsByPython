

from abc import ABCMeta, abstractmethod


class Product:

  def __init__(self) -> None:
    self.name = ""
    self.category = ""

  def __str__(self) -> str:
    return f"{self.name}, {self.category}"

class ProductBuilder(metaclass=ABCMeta):

  @abstractmethod
  def __init__(self) -> None:
    self.product = Product()

  @abstractmethod
  def build_name(self):
    pass

  @abstractmethod
  def build_category(self):
    pass

  @abstractmethod
  def product(self):
    pass

  
class CarBuidler(ProductBuilder):
  
  def __init__(self) -> None:
      self.product = Product()

  def build_name(self):
    self.product.name = "本田"
    print("name: car builded!")

  def build_category(self):
    self.product.category = "乗り物"
    print("category: car builded!")

class Director:
  def __init__(self, b: ProductBuilder) -> None:
      self.b = b
  
  def build(self):
    self.b.build_name()
    self.b.build_category()

  def builder(self):
    return self.b

cb = CarBuidler()

d = Director(cb)

d.build()
print(d.builder().product)