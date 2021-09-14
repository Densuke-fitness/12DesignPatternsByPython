from abc import ABCMeta, abstractclassmethod

class Athlete(metaclass=ABCMeta):
  pass


class SwimAthlete(Athlete):
  @abstractclassmethod
  def swim(self):
    pass

class JumpAthlete(Athlete):
  @abstractclassmethod
  def high_jump(self):
    pass

  @abstractclassmethod
  def long_jump(self):
    pass


class Athlete1(SwimAthlete):

  def swim(self):
      print("athlete1 swim")

class Athlete2(SwimAthlete, JumpAthlete):

  def swim(self):
      print("athlete2 swim")

  def high_jump(self):
      print("athlete2 high_jump")
  
  def long_jump(self):
    print("athlete2 long_jump")


a1 = Athlete1()
a1.swim()

a2 = Athlete2()
a2.swim()
a2.long_jump()