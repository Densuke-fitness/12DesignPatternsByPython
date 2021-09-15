from abc import ABCMeta, abstractmethod

class Component(metaclass=ABCMeta):

  @abstractmethod
  def operarion(self):
    pass

class CharComponent(Component):
  
  def __init__(self, char: str):
    self.char = char

  def operarion(self):
      print(self.char * 20)

class Decorator(Component):

  def __init__(self, component: Component):
    self.component = component

class Message(Decorator):

  def __init__(self, component: Component, msg):
      super().__init__(component)
      self.msg = msg

  def operarion(self):
    self.component.operarion()
    print(self.msg)
    self.component.operarion()


cc = CharComponent("✨")

m = Message(cc, "こんにちは")
m.operarion()