from abc import ABC, abstractmethod


class MenuItem:
	def __init__(self, name, desc, vegetarian, price):
		self.name = name
		self.desc = desc
		self.vegetarian = vegetarian
		self.price = price

	def __str__(self):
		return f'{self.name} - {self.desc}'


class Menu(ABC):
	@abstractmethod
	def create_iterator(self): ...


class PanCakeHouseMenu(Menu):
	def __init__(self):
		self.items = {}

		self.add_item('Шаурма', 'Шаурма по кавказски', False, 190)
		self.add_item('Бургер', 'Бургер грант шеф стронг хрен пор там', False, 560)

	def add_item(self, name, desc, vegetarian, price):
		item = MenuItem(name, desc, vegetarian, price)
		self.items[name] = item

	def create_iterator(self):
		return iter(self.items.values())


class DinerMenu(Menu):
	def __init__(self):
		self.items = []
		self.add_item('Лосось', 'Лосоль халяль', False, 850)
		self.add_item('Салат', 'Салат из травы', True, 8500)

	def add_item(self, name, desc, vegetarian, price):
		item = MenuItem(name, desc, vegetarian, price)
		self.items.append(item)

	def create_iterator(self):
		return iter(self.items)


class Officiant:
	def __init__(self):
		self.menus: list[Menu] = [DinerMenu(), PanCakeHouseMenu()]

	def print_menu(self):
		for i in self.menus:
			[print(item) for item in i.create_iterator()]


# В питоне уже есть итераторы. Можно не реализовывать кучу доп. классов. Но ВАЖНО выделить все меню в интерфейс,
# чтобы оставаться на уровне интерфейсов, а не переходить в реализацию.
o = Officiant()
o.print_menu()
