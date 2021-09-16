# from abc import ABCMeta, abstractmethod

# class DatingStrategy(metaclass=ABCMeta):

#   @abstractmethod
#   def execute(self):
#     pass

# class OraOraKei(DatingStrategy):

#   def execute(self):
#       for i in range(10):
#         if i % 4 == 0 :
#           print("メッチャきまってるやんけ！")
#         print("オイ!")

# class SKei(DatingStrategy):

#   def execute(self):
#     for i in range(10):
#         if i % 3 == 0 :
#           print("でも、そういうところ僕は好きだよ")
#         print("ふーん, 別に。")

# class SeiZitsuKei(DatingStrategy):

#   def execute(self):
#     for i in range(10):
#         if i % 3 == 0 :
#           print("めっちゃタイプ")
#         print("そうなんだ！えーいいじゃん！")
      
# class Context:

#   def __init__(self) -> None:
#       self.skei = SKei()
#       self.oraorakei = OraOraKei()
#       self.seizitsuteki = SeiZitsuKei()

#   def act(self, gril_type):

#     if gril_type == "ツンデレ":
#       self.skei.execute()
#     elif gril_type == "勝気":
#       self.oraorakei.execute()
#     else:
#       self.seizitsuteki.execute()


# c = Context()
# c.act("kpop")


#比較としてstateも実装
from abc import ABCMeta, abstractmethod

class WorkingState(metaclass=ABCMeta):

  @abstractmethod
  def work(self):
    pass

  @abstractmethod
  def after_work(self):
    pass

class DayState(WorkingState):

  def work(self):
      print("よっし、朝から働くぞー！")

  def after_work(self):
      print("サ活すっか")

class NightState(WorkingState):

  def work(self):
      print("シンプルに眠い")

  def after_work(self):
      print("zzzzzzz")

class Context:


  def __init__(self) -> None:
    self._working_state = DayState()

  def change_state(self, working_state: WorkingState):
    self._working_state = working_state

  def execute(self):
    print("仕事前")
    self._working_state.work()
    print("仕事後")
    self._working_state.after_work()
c = Context()
c.execute()

c.change_state(NightState())
c.execute()