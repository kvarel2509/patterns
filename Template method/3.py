from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
	def prepare_recipe(self):
		self.boil_water()
		self.hook1()
		self.brew()
		self.hook2()
		self.pour_in_cup()
		if self.hook3():
			self.add_condiments()
		self.hook4()

	def boil_water(self):
		print('Boiling water')

	def pour_in_cup(self):
		print('Pouring into cup')

	# Хуки позволяют добавить в алгоритм новые шаги. Если их переопределит дочерний класс, алгоритм может измениться.
	# Можно их не трогать, в этом случае алгоритм останется не тронут.
	def hook1(self): ...

	def hook2(self): ...

	def hook3(self):
		return True

	def hook4(self): ...

	@abstractmethod
	def brew(self): ...

	@abstractmethod
	def add_condiments(self): ...


class Tea(CaffeineBeverage):
	def __init__(self):
		self.counter = 0
		self.limit = 10

	def brew(self):
		print('Steeping the tea')

	# Здесь заложена дополнительная логика. Перехвачены hook3 и hook4
	def hook4(self):
		self.counter += 1

	def hook3(self):
		return self.counter < self.limit

	def add_condiments(self):
		print('Adding lemon')


class Coffee(CaffeineBeverage):
	def brew(self):
		print('Dripping coffee through filter')

	def add_condiments(self):
		print('Adding sugar and milk')

	# Здесь хуки не перехватывались

