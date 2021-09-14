# from abc import ABCMeta, abstractclassmethod


# class Book:
#   def  __init__(self, content) -> None:
#       self.content = content

# class Formatter(metaclass=ABCMeta):
  
#   @abstractclassmethod
#   def format(self, book: Book):
#     pass

# class AFormatter(Formatter):

#   def format(self, book: Book):
#       return book.content + "A"


# class BFormatter(Formatter):

#   def format(self, book: Book):
#       return book.content + "B"

# class Printer:

#   def __init__(self, formatter: Formatter) -> None:
#     self.formatter = formatter

#   def print(self, book):
#     print(self.formatter.format(book))

# b = Book("content")

# ap = Printer(AFormatter())
# ap.print(b)

# bp = Printer(BFormatter())
# bp.print(b)

from abc import ABCMeta, abstractclassmethod, abstractmethod, abstractproperty

class IBook(metaclass=ABCMeta):

  #contentという名前のゲッターを生成しないといけないpropertyにcontentnを持たんといけない
  @abstractproperty
  def content(self):
    pass


class Book(IBook):

  def __init__(self, content) -> None:
      self._content = content

  @property
  def content(self):
    return self._content

class EBook(IBook):

  def __init__(self, content) -> None:
      self._content = content

  @property
  def content(self):
    return self._content



class IFormatter(metaclass=ABCMeta):

  #抽象クラスを引数にもつ
  @abstractmethod
  def format(self, i_book: IBook):
    pass


class HtmlFormatter(IFormatter):

  def format(self, i_book: IBook):
    return '<h1>' + i_book.content + '</h1>'


class XmlFormatter(IFormatter):

  def format(self, i_book: IBook):
    return '<xml>' + i_book.content + '</xml>'



class Printer:

  #集約(単一責任の原則を遵守)を記載する際も抽象化する 
  def __init__(self, i_formatter :IFormatter) -> None:
    self._i_formatter = i_formatter
  
  #引数を抽象化させる
  def print(self, i_book :IBook):
    formatted_book = self._i_formatter.format(i_book)
    print(formatted_book)

hf = HtmlFormatter()
b = Book("content: Python")

e = EBook("content: Kindle")

xml = XmlFormatter()
p1 = Printer(hf)
p1.print(b)

p2 = Printer(xml)
p2.print(b)

p2.print(e)
