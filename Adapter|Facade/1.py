from abc import ABC, abstractmethod


class Duck(ABC):
	@abstractmethod
	def quack(self): ...

	@abstractmethod
	def fly(self): ...


class Turkey(ABC):
	@abstractmethod
	def gobble(self): ...

	@abstractmethod
	def fly(self): ...
# ----------------------------------------------------------------------


class TurkeyAdapter(Duck):
	def __init__(self, turkey: Turkey):
		self.turkey = turkey

	def quack(self):
		self.turkey.gobble()

	def fly(self):
		[self.turkey.fly() for _ in range(2)]


class DuckAsTurkeyAdapter(Turkey):
	def __init__(self, duck: Duck):
		self.__duck = duck

	def gobble(self):
		self.__duck.quack()

	def fly(self):
		self.__duck.fly()
		print('На короткие дистанции')


class TurkeyAsDuckAdapterClass(Turkey, Duck):
	def gobble(self):
		super().gobble()

	def fly(self):
		self.fly()

	def quack(self):
		self.gobble()


# ----------------------------------------------------------------------


class MallardDuck(Duck):
	def quack(self):
		print('Кря')

	def fly(self):
		print('Я лечу')


class WildTurkey(Turkey):
	def gobble(self):
		print('gobble gobble')

	def fly(self):
		print('I aa flying a short distance')


class TestDuck:
	def __init__(self, duck: Duck):
		self.__duck = duck

	def test(self):
		self.__duck.quack()
		self.__duck.fly()


class TestTurkey:
	def __init__(self, turkey: Turkey):
		self.__turkey = turkey

	def test(self):
		self.__turkey.gobble()
		self.__turkey.fly()


a = MallardDuck()
b = WildTurkey()
c = TurkeyAdapter(b)
d = DuckAsTurkeyAdapter(a)
e = TurkeyAsDuckAdapterClass()


# Turkey становится Duck не только сопоставлением методов. Это кстати похоже на логику работы паттерна
# команда. Но и приобретает тип Duck.
