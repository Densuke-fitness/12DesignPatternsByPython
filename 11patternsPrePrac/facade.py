class Container:

  def __init__(self, *args) -> None:
    self.cls_list = [*args]

  def execute(self):
    for cls in  self.cls_list:
      cls.do()

class  Cook:

  def __init__(self, container :Container):
    self.container = container

  def execute(self):
    self.container.execute()

class Frier:

  def __init__(self, name) -> None:
      self.name = name

  def do(self):
    print(f"fry : {self.name}")

class Cuter:

  def __init__(self, name) -> None:
      self.name = name

  def do(self):
    print(f"cut : {self.name}")

class Boiler:

  def __init__(self, name) -> None:
      self.name = name

  def do(self):
    print(f"boil : {self.name}")


c = Container(Boiler("野菜"), Cuter("魚"), Frier("肉"))

cook = Cook(c)
cook.execute()