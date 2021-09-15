from abc import ABCMeta, abstractmethod

#ServiceとMapAPI

class IMapApi(metaclass=ABCMeta):

  #ポリモーフィックな処理
  def execute(self, token: str):
    self.connect()
    print(token)
    self.diconnect()

  @abstractmethod
  def connect(self):
    pass

  @abstractmethod
  def diconnect(self):
    pass

class GoogleMapApi(IMapApi):

  def connect(self):
    print("g connected")


  def diconnect(self):
    print("g disconnected")


class YahooMapApi(IMapApi):

  def connect(self):
    print("y connected")


  def diconnect(self):
    print("y disconnected")


class IService(metaclass=ABCMeta):

  @abstractmethod
  def call_api(self):
    return IMapApi()

class GoogleService(IService):

  def call_api(self):
      return GoogleMapApi()

class YahooService(IService):

  def call_api(self):
      return YahooMapApi()



gs = GoogleService()
gs.call_api().execute("gfagajwrkoabw")

print("-"*20)
ys = YahooService()
ys.call_api().execute("124e-13rgvaw")