from abc import ABC, abstractmethod


class Pizza(ABC):
	name: str
	dough: str
	sauce: str
	toppings: list

	def prepare(self):
		print(f'Начинаем готовить пиццу {self.name}')
		print('Замешиваем тесто')
		print('Добавляем соус')
		print('Добавляем добавки')
		[print(topping) for topping in self.toppings]

	def bake(self):
		print('Выпекаем 20 минут')

	def cut(self):
		print('Нарезаем треугольниками')

	def box(self):
		print('Фирменно упаковываем')


class PizzaStore:
	def order_pizza(self, type_pizza):
		pizza = self.create_pizza(type_pizza)
		pizza.prepare()
		pizza.bake()
		pizza.cut()
		pizza.box()
		return pizza

	@abstractmethod
	def create_pizza(self, type_pizza: str): ...


class MoscowFourCheesePizza(Pizza):
	name = 'Московский вариант пиццы 4 сыра'
	dough = 'Тонкое тесто'
	sauce = 'Соус Балтимор'
	toppings = ['грибы', 'помидоры']

	def bake(self):
		print('Выпекаем 10 минут')


class MoscowMargaritaPizza(Pizza):
	name = 'Московский вариант пиццы Маргарита'
	dough = 'Тонкое тесто'
	sauce = 'Соус балтимор'
	toppings = ['грибы']


class PenzaFourCheesePizza(Pizza):
	name = 'Пензенский вариант пиццы 4 сыра'
	dough = 'Толстое тесто'
	sauce = 'Соус домашний'
	toppings = ['огурчики']

	def bake(self):
		print('Выпекаем 30 минут')


class PenzaMargaritaPizza(Pizza):
	name = 'Пензенский вариант пиццы Маргарита'
	dough = 'Толстое тесто'
	sauce = 'Соус домашний'
	toppings = ['огурчики']

	def bake(self):
		print('Выпекаем 30 минут')


class MoscowPizzaStore(PizzaStore):
	PIZZA_MATCHING = {'four_cheese': MoscowFourCheesePizza, 'margarita': MoscowMargaritaPizza}

	def create_pizza(self, type_pizza: str):
		pizza = self.PIZZA_MATCHING.get(type_pizza)
		if pizza:
			return pizza()
		raise ValueError('Нет такой пиццы')


class PenzaPizzaStore(PizzaStore):
	PIZZA_MATCHING = {'four_cheese': PenzaFourCheesePizza, 'margarita': PenzaMargaritaPizza}

	def create_pizza(self, type_pizza: str):
		pizza = self.PIZZA_MATCHING.get(type_pizza)
		if pizza:
			return pizza()
		raise ValueError('Нет такой пиццы')


penza_store = PenzaPizzaStore()
penza_store.order_pizza('margarita')

moscow_store = MoscowPizzaStore()
moscow_store.order_pizza('four_cheese')

# Здесь реализуется фабричный метод. Создаются разные классы магазинов, которые переопределяют этот метод.
# Реализация выбирается субклассами. Фабричный метод очень похож на Простую фабрику, но дает более гибкий подход
# к созданию объектов.
