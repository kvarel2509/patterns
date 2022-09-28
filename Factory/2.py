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


class PizzaStore:
	def __init__(self, factory):
		self.factory = factory

	def order_pizza(self, type_pizza):
		"""
		В этом месте можно декорировать объекты и возвращать готовый
		"""
		pizza = self.factory.create_pizza(type_pizza)
		pizza.prepare()
		pizza.bake()
		pizza.cut()
		pizza.box()
		return pizza


class MoscowFourCheesePizza(Pizza):
	def prepare(self):
		print('prepare MOSCOW four cheese pizza')

	def bake(self):
		print('bake MOSCOW four cheese pizza')

	def cut(self):
		print('cut MOSCOW four cheese pizza')

	def box(self):
		print('box MOSCOW four cheese pizza')


class MoscowMargaritaPizza(Pizza):
	def prepare(self):
		print('prepare MOSCOW margarita pizza')

	def bake(self):
		print('bake MOSCOW margarita pizza')

	def cut(self):
		print('cut MOSCOW margarita pizza')

	def box(self):
		print('box MOSCOW margarita pizza')


class PenzaFourCheesePizza(Pizza):
	def prepare(self):
		print('prepare PENZA four cheese pizza')

	def bake(self):
		print('bake PENZA four cheese pizza')

	def cut(self):
		print('cut PENZA four cheese pizza')

	def box(self):
		print('box PENZA four cheese pizza')


class PenzaMargaritaPizza(Pizza):
	def prepare(self):
		print('prepare PENZA margarita pizza')

	def bake(self):
		print('bake PENZA margarita pizza')

	def cut(self):
		print('cut PENZA margarita pizza')

	def box(self):
		print('box PENZA margarita pizza')


class MoscowPizzaFactory:
	PIZZA_MATCHING = {'four_cheese': MoscowFourCheesePizza, 'margarita': MoscowMargaritaPizza}

	def create_pizza(self, type_pizza: str):
		pizza = self.PIZZA_MATCHING.get(type_pizza)
		if pizza:
			return pizza()
		raise ValueError('Нет такой пиццы')


class PenzaPizzaFactory:
	PIZZA_MATCHING = {'four_cheese': PenzaFourCheesePizza, 'margarita': PenzaMargaritaPizza}

	def create_pizza(self, type_pizza: str):
		pizza = self.PIZZA_MATCHING.get(type_pizza)
		if pizza:
			return pizza()
		raise ValueError('Нет такой пиццы')


penza_factory = PenzaPizzaFactory()
penza_store = PizzaStore(penza_factory)

moscow_factory = MoscowPizzaFactory()
moscow_store = PizzaStore(moscow_factory)

penza_store.order_pizza('margarita')
moscow_store.order_pizza('four_cheese')

# Здесь реализуется класс фабрики, которая передается магазину. Дальше магазин будет обращаться к этой фабрике
# для создания экземпляров класса.
# Простая фабрика конечно инкапсулирует поведение создания объекта, но она делает это более прямолинейно.
# И дает меньше гибкости
