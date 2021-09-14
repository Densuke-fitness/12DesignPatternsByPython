# class UserInfo:

#   def __init__(self, user_name, job_name, nationality) -> None:
#     self.user_name = user_name
#     self.job_name = job_name
#     self.nationality = nationality


#   def __str__(self) -> str:
#       return f"{self.user_name}, {self.job_name}, {self.nationality}"


# class UserInfoFilter:

#   @staticmethod
#   def filter_users_job(users, job_name):
#     for user in users:
#       if user.job_name == job_name:
#         yield user
  
#   @staticmethod
#   def filter_users_job(users, nationality):
#     for user in users:
#       if user.nationality == nationality:
#         yield user
      

# taro = UserInfo("taro", "engineer", "Japan")
# jiro = UserInfo("taro", "sales", "Japan")
# saburo = UserInfo("taro", "engineer", "Usa")

# user_list = [taro, jiro, saburo]

# for man in UserInfoFilter.filter_users_job(user_list, "Japan"):
#   print(man) 
from abc import ABCMeta, abstractclassmethod

class UserInfo:

  def __init__(self, user_name, job_name, nationality) -> None:
    self.user_name = user_name
    self.job_name = job_name
    self.nationality = nationality

  def __str__(self) -> str:
    return f"{self.user_name}, {self.job_name}, {self.nationality}"


class Comparation(metaclass=ABCMeta):

  @abstractclassmethod
  def is_equal(self, other):
    pass

  def __and__(self, other):
    #ここでselfを第一引数に入れてるけど=>AndComparation的には  (self, Comparationのself, otherのself)と第二引数以降になる
    return AndComparation(self, other)

  def __or__(self, other):
    return OrComparation(self, other)


class AndComparation(Comparation):

  #ここで全ての比較条件をまとめている
  def __init__(self, *args) -> None:
    self.comparations = args

  def is_equal(self, other):
    #ここで全ての比較条件を行いマッチしたのみのuserを返却
      #=>filterでAndComparationが回された時にこの関数がよばれる(otherはuser)
      #セットされた比較条件comparationsがmapされる
    return all(
      map(lambda comparation: comparation.is_equal(other), self.comparations)
    )
      

class OrComparation(Comparation):

  def __init__(self, *args) -> None:
    self.comparations = args

  def is_equal(self, other):
    return any(
      map(lambda comparation: comparation.is_equal(other), self.comparations)
    )


class Filter(metaclass=ABCMeta):

  @abstractclassmethod
  def filter(self, comparation, items):
    pass



class JobNameComp(Comparation):

  def __init__(self, job_name) -> None:
      self.job_name =job_name

  def is_equal(self, other):
    return self.job_name == other.job_name


class NationalityComp(Comparation):

  def __init__(self, nationality) -> None:
      self.nationality = nationality

  def is_equal(self, other):
      return self.nationality == other.nationality

class UserInfoFilter(Filter):

  def filter(self, comparation, items):
      for item in items:
        if comparation.is_equal(item):
          yield item

taro = UserInfo("taro", "engineer", "Japan")
jiro = UserInfo("taro", "sales", "Japan")
saburo = UserInfo("taro", "engineer", "Usa")
user_list = [taro, jiro, saburo]

engineer_comp = JobNameComp("engineer")
japan_comp = NationalityComp("Japan")
user_info_filter = UserInfoFilter()

engineer_and_japan = engineer_comp & japan_comp

engineer_or_japan = engineer_comp | japan_comp
# for user in user_info_filter.filter(engineer_comp, user_list):
#   print(user)

# for user in user_info_filter.filter(engineer_and_japan, user_list):
#   print(user)

for user in user_info_filter.filter(engineer_or_japan, user_list):
  print(user)
