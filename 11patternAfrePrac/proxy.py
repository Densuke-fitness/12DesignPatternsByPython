from abc import ABCMeta, abstractmethod
import time

class ApiCaller:

  def __init__(self, url) -> None:
      self._url = url

  @abstractmethod
  def request(self):
    pass

class RealApiCaller(ApiCaller):

  def __init__(self, url) -> None:
      #思い処理
      super().__init__(url)

  def request(self):
      print("リクエストを送ります")
      time.sleep(5)
      print("レスポンスが届きました")

class ProxyApiCaller(ApiCaller):

  def __init__(self, url) -> None:
      super().__init__(url)

  def request(self):
      if self._check_access():
        real_api_caller = RealApiCaller(self._url)
        real_api_caller.request()
        self._write_log()

  def _check_access(self):
    print("アクセスに成功しました")
    return True

  def _write_log(self):
    print("logを出力します")

url = "https://api.com"

pa = ProxyApiCaller(url)
pa.request()