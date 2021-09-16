from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):

  @abstractmethod
  def _execute(self):
    pass


class RealSubject(Subject):

  def _execute(self):
      print("execute real subject")

class Proxy(Subject):

  def __init__(self) -> None:
    self.rs = RealSubject()

  def handle(self, num):
    if num > 100 :
      self.rs._execute() 
    else:
      self._execute()


  def _execute(self):
    print("execute proxy subject")

  

p = Proxy()

p.handle(10)
p.handle(1000)

