class UserInfo:

  ## User情報を保持するクラス
  def __init__(self, name, age) -> None:
      self.name = name 
      self.age = age
  
  def __str__(self) -> str:
      return f"{self.name}: {self.age}"


class FileManager:

  #オブジェクトのstr情報を書き込むもの
  @staticmethod
  def write_str_to_file(obj, filename):
    with open(filename, "w") as f:
      f.write(str(obj))

#ファイル書き込みの役割と, 対象となる情報　を分けて責務を分離
FileManager.write_str_to_file(UserInfo("Yusuke", 22), "test.txt")
