from abc import ABCMeta, abstractmethod


#notifyをキャッチしたObserverが処理をする
class Observer(metaclass=ABCMeta):

  @abstractmethod
  def act(self):
    pass

class TwitterLikeObserver(Observer):

  def act(self, s):
    s.execute()
    print(f"{s}のtwitterのをいいねを確認しました")


class TwitterRetweetObserver(Observer):

  def act(self, s):
    s.execute()
    print(f"{s}のtwitterのをリツイートを確認しました")


#ざぶジェクト側がnotifyをして伝える
class Subject(metaclass=ABCMeta):

  def __init__(self, name) -> None:
      self._observers = []
      self._name = name
  
  def __str__(self) -> str:
      return f"subject:{self._name}"

  def notify(self):
    for obs in self._observers:
      obs.act(self)

  def attach(self, observer :Observer):
    self._observers.append(observer)
    print("アタッチしました")
  
  def detach(self, observer :Observer):
    self._observers.remove(observer)
    print("デタッチしました")

  @classmethod
  def execute(self):
    pass

class TwitterSubject(Subject):
  
  def __init__(self, name) -> None:
      super().__init__(name)

  def execute(self):
    print("twitterを実行しました")

  def like(self):
    print("like")
    self.notify()

tlo = TwitterLikeObserver()
tro = TwitterRetweetObserver()

ts = TwitterSubject("Densuke")

ts.attach(tlo)
ts.attach(tro)

ts.like()