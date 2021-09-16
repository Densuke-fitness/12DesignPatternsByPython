from abc import ABCMeta, abstractmethod

class Greeting(metaclass=ABCMeta):
  def __init__(self, name) -> None:
      self._name = name

  def greet(self):
    self._first_greet()
    self._body_greet()
    self._last_gereet()
    self._additional_greet()

  
  @abstractmethod
  def _first_greet(self):
    pass

  @abstractmethod
  def _body_greet(self):
    pass  
  
  @abstractmethod
  def _last_gereet(self):
    pass  
  
  #追加で話しない内容があるとき
  def _additional_greet(self):
    pass

class Formal(Greeting):
  def __init__(self, name) -> None:
      super().__init__(name)


  def _first_greet(self):
      print(f"お久しぶりです。{self._name}さん、お元気でしたか")
      
  def _body_greet(self):
      print(f"この前の件について{self._name}さんの方にお聞きしたいことがあるのですが今って、お時間少し頂くことはできますでしょうか。")

  def _last_gereet(self):
    print(f"{self._name}さんこの度はありがとうございました、特に〜の部分に関しましては大変助かりました。今後ともよろしくお願いいたします")
      

  
class Casual(Greeting):
  def __init__(self, name) -> None:
      super().__init__(name)


  def _first_greet(self):
      print(f"おひさ！え〜{self._name}めっちゃ元気そうやん、最近はどっすか！💪")
      
  def _body_greet(self):
      print(f"そうそう、ちょっとね〜これに{self._name}しか聞けなそうな案件があってさー、今ってちょっとだけ聞く時間てない、、？すまねえ！")

  def _last_gereet(self):
      print(f"まじで{self._name}には助かった！ほんまありがとうまたよろしくっす〜！！今度飲み行こうぜ！")


  def _additional_greet(self):
      print("新橋に行きつけの焼き鳥屋さんあるんよw")

  

fg = Formal("お偉いさん")

cg = Casual("友達さん")

fg.greet()

cg.greet()