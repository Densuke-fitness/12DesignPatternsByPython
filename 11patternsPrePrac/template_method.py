from abc import ABCMeta, abstractmethod

class Validator(metaclass=ABCMeta):

  @abstractmethod
  def validate(self):
    pass

class IntegerValidator(Validator):

  def validate(self, num):
      if num > 10:
        print("error integer")

class StringValidator(Validator):

  def validate(self, word):
      if word == "":
        print("error string")


iv = IntegerValidator()
iv.validate(12)

sv = StringValidator()
sv.validate("")