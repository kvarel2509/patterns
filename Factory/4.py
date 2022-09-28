from abc import ABC, abstractmethod


class Dough(ABC):
	name: str


class Sauce(ABC):
	name: str


class Cheese(ABC):
	name: str


class Clap(ABC):
	name: str


class PomidorClap(Clap):
	name = 'Помидорчики'


class ThinCrustDough(Dough):
	name = 'Тонкое тесто'


class MarinaraSauce(Sauce):
	name = 'Соус маринара'


class ReggianoCheese(Cheese):
	name = 'Сыр Регианно'


class MaheevSauce(Sauce):
	name = 'Соус Махеев'


class FetaCheese(Cheese):
	name = 'Сыр фета'


class PizzaIngredientFactory(ABC):
	@abstractmethod
	def create_dough(self): ...

	@abstractmethod
	def create_sauce(self): ...

	@abstractmethod
	def create_cheese(self): ...

	@abstractmethod
	def create_clap(self): ...


class PenzaPizzaIngredientFactory(PizzaIngredientFactory):
	def create_dough(self):
		return ThinCrustDough()

	def create_sauce(self):
		return MarinaraSauce()

	def create_cheese(self):
		return ReggianoCheese()

	def create_clap(self):
		return PomidorClap()


class MoscowPizzaIngredientFactory(PizzaIngredientFactory):
	def create_dough(self):
		return ThinCrustDough()

	def create_sauce(self):
		return MaheevSauce()

	def create_cheese(self):
		return ReggianoCheese()

	def create_clap(self):
		return PomidorClap()


class Pizza(ABC):
	name: str
	dough: Dough
	sauce: Sauce
	cheese: Cheese
	clap: Clap

	@abstractmethod
	def prepare(self): ...

	def bake(self):
		print('Выпекать 25 минут при 350 градусах')

	def cut(self):
		print('Нарезать треугольниками')

	def box(self):
		print('Упаковать в брендовую упаковку')


class PizzaStore(ABC):
	ingredient_factory: PizzaIngredientFactory

	def order_pizza(self, type_pizza):
		pizza = self.create_pizza(type_pizza)
		pizza.prepare()
		pizza.bake()
		pizza.cut()
		pizza.box()
		return pizza

	@abstractmethod
	def create_pizza(self, type_pizza: str): ...


class MargaritaPizza(Pizza):
	name = 'Маргарита'

	def __init__(self, ingredient_factory: PizzaIngredientFactory):
		self.ingredient_factory = ingredient_factory

	def prepare(self):
		print(f'Начинаем подготовку пиццы {self.name}')
		self.dough = self.ingredient_factory.create_dough()
		self.sauce = self.ingredient_factory.create_sauce()
		self.cheese = self.ingredient_factory.create_cheese()
		self.clap = self.ingredient_factory.create_clap()
		print(f'Используем {self.dough.name}, {self.sauce.name}, {self.cheese.name}, {self.clap.name}')


class FourCheesePizza(Pizza):
	name = '4 сыра'

	def __init__(self, ingredient_factory: PizzaIngredientFactory):
		self.ingredient_factory = ingredient_factory

	def prepare(self):
		print(f'Начинаем подготовку пиццы {self.name}')
		self.dough = self.ingredient_factory.create_dough()
		self.cheese = self.ingredient_factory.create_cheese()
		self.clap = self.ingredient_factory.create_clap()
		print(f'Используем {self.dough.name}, {self.cheese.name}, {self.clap.name}')


class PenzaPizzaStore(PizzaStore):
	PIZZA_MATCHING = {'four_cheese': FourCheesePizza, 'margarita': MargaritaPizza}
	ingredient_factory = PenzaPizzaIngredientFactory()

	def create_pizza(self, type_pizza: str):
		pizza = self.PIZZA_MATCHING.get(type_pizza)
		if pizza:
			return pizza(self.ingredient_factory)
		raise ValueError('Нет такой пиццы')


class MoscowPizzaStore(PizzaStore):
	PIZZA_MATCHING = {'four_cheese': FourCheesePizza, 'margarita': MargaritaPizza}
	ingredient_factory = MoscowPizzaIngredientFactory()

	def create_pizza(self, type_pizza: str):
		pizza = self.PIZZA_MATCHING.get(type_pizza)
		if pizza:
			return pizza(self.ingredient_factory)
		raise ValueError('Нет такой пиццы')


store = PenzaPizzaStore()
store.order_pizza('margarita')

print('-----------------')

store = MoscowPizzaStore()
store.order_pizza('margarita')
