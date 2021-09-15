class Singleton:
  __instance = None

  def __new__(cls):
    if cls.__instance is None:
      #基底クラスのobjectクラスを呼び出すsuper()でも可能=>親クラスが子クラスのインスタンスを生成する時にええんかね 
      # cls.__instance = object.__new__(cls)
      cls.__instance = super().__new__(Tmp)
    return  cls.__instance

class Tmp:
  pass

i1 = Singleton()
i2 = Singleton()

print(type(i1))
print(type(i2))