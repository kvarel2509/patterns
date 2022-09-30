class MenuItem:
	def __init__(self, name, desc, vegetarian, price):
		self.name = name
		self.desc = desc
		self.vegetarian = vegetarian
		self.price = price

	def __str__(self):
		return f'{self.name} - {self.desc}'


class PanCakeHouseMenu:
	def __init__(self):
		self.items = []

		self.add_item('Шаурма', 'Шаурма по кавказски', False, 190)
		self.add_item('Бургер', 'Бургер грант шеф стронг хрен пор там', False, 560)

	def add_item(self, name, desc, vegetarian, price):
		item = MenuItem(name, desc, vegetarian, price)
		self.items.append(item)

	def get_menu_items(self):
		return self.items


class DinerMenu:
	def __init__(self):
		self.items = set()
		self.add_item('Лосось', 'Лосоль халяль', False, 850)
		self.add_item('Салат', 'Салат из травы', True, 8500)

	def add_item(self, name, desc, vegetarian, price):
		item = MenuItem(name, desc, vegetarian, price)
		self.items.add(item)

	def get_menu_items(self):
		return self.items


class Officiant:
	def __init__(self):
		self.pancake = PanCakeHouseMenu()
		self.diner = DinerMenu()

	def print_menu(self):
		pancake_items = self.pancake.get_menu_items()
		diner_items = self.diner.get_menu_items()
		# Разные типы! Что делать? Нельзя объединить. А если объектов станет больше?

		[print(item) for item in pancake_items]
		[print(item) for item in diner_items]
		# Количество циклов будет расти


o = Officiant()
o.print_menu()
