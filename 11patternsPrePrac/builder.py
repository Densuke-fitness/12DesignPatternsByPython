from abc import ABCMeta, abstractmethod, abstractproperty

class IProduct(metaclass=ABCMeta):

  @abstractproperty
  def content(self):
    pass

class ConcleteProduct1(IProduct):

  def __init__(self, content) -> None:
      self._content = content + ": 1"

  @property
  def content(self):
    return self._content

class ConcleteProduct2(IProduct):

  def __init__(self, content) -> None:
      self._content = content + ": 2"

  @property
  def content(self):
    return self._content

class Builder(metaclass=ABCMeta):

  @abstractmethod
  def build_part(self, i_product: IProduct):
    return i_product

class ConcreteBuilder1(Builder):

  def build_part(self, i_product: IProduct):
      return i_product.content + ": concrete builder1"


class ConcreteBuilder2(Builder):

  def build_part(self, i_product: IProduct):
      return i_product.content + ": concrete builder2"

class Director:

  def __init__(self, builder: Builder) -> None:
      self.builder = builder

  def construct(self, i_product: IProduct):
    print(self.builder.build_part(i_product))

cp2 = ConcleteProduct2("content")

cb1 = ConcreteBuilder1()

d = Director(cb1)

d.construct(cp2)
