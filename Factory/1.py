from abc import ABC, abstractmethod


class Pizza(ABC):
	@abstractmethod
	def prepare(self): ...

	@abstractmethod
	def bake(self): ...

	@abstractmethod
	def cut(self): ...

	@abstractmethod
	def box(self): ...


class FourCheesePizza(Pizza):
	def prepare(self):
		print('prepare four cheese pizza')

	def bake(self):
		print('bake four cheese pizza')

	def cut(self):
		print('cut four cheese pizza')

	def box(self):
		print('box four cheese pizza')


class MargaritaPizza(Pizza):
	def prepare(self):
		print('prepare margarita pizza')

	def bake(self):
		print('bake margarita pizza')

	def cut(self):
		print('cut margarita pizza')

	def box(self):
		print('box margarita pizza')


class SimplePizzaFactory:
	"""
	Смысл этого класса - чтобы в глобальной области видимости исключить работу с конкретными классами.
	Создание экземпляра пиццы инкапсулируется на фабрике.
	Иначе может так случиться, что код создания экземпляра класса будет дублироваться в разных местах.
	"""
	PIZZA_MATCHING = {'four_cheese': FourCheesePizza, 'margarita': MargaritaPizza}

	def create_pizza(self, type_pizza: str):
		pizza = self.PIZZA_MATCHING.get(type_pizza)
		if pizza:
			return pizza()
		else:
			raise ValueError('Нет такой пиццы')

# В этом варианте дочерние классы пиццы имеют каждый свою реализацию приготовления пиццы.
# Общий только функционал ее создания.