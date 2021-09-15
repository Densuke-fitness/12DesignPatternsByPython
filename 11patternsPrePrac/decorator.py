from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):

  @abstractmethod
  def execute(self):
    pass

class Decorator(Component):

  def __init__(self, component: Component) -> None:
      self.component = component

  @abstractmethod
  def execute(self):
      pass

class ConcreteComponent(Component):

  def execute(self):
      print("execute!!")

class StarDecorator(Decorator):

  def __init__(self, component: Component) -> None:
      super().__init__(component)

  
  def execute(self):
      print("✨"* 10)
      self.component.execute()
      print("✨"* 10)

  
cc = ConcreteComponent()
sd = StarDecorator(cc)

sd.execute()
