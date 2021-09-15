from abc import ABCMeta, abstractmethod

class Vehicle(metaclass=ABCMeta):

  @abstractmethod
  def run(self):
    pass

  def stop(self):
    pass


class Car(Vehicle):

  def __init__(self, name) -> None:
      self.name = name

  def run(self):
    print(f"car: {self.name} run")

  def stop(self):
    print(f"car: {self.name} stop")


class Driver(metaclass=ABCMeta):
  
  @abstractmethod
  def use(self):
    pass


class CarDriver(Driver):

  def __init__(self, car: Car) -> None:
      self.car = car
    
  def use(self):
      print("車を走らせます")
      self.car.run()
      print("進みます")
      print("車を止めます")
      self.car.stop()



c_h = Car("本田")
c_t = Car("トヨタ")

CarDriver(c_h).use()
CarDriver(c_t).use()