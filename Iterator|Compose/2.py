from abc import ABC, abstractmethod


class MenuItem:
	def __init__(self, name, desc, vegetarian, price):
		self.name = name
		self.desc = desc
		self.vegetarian = vegetarian
		self.price = price

	def __str__(self):
		return f'{self.name} - {self.desc}'


class Iterator(ABC):
	@abstractmethod
	def has_next(self): ...

	@abstractmethod
	def next(self): ...


class DinerMenuIterator(Iterator):
	def __init__(self, items):
		self.position = 0
		self.items = items

	def has_next(self):
		return self.position < len(self.items)

	def next(self):
		item = self.items[self.position]
		self.position += 1
		return item


class PanCakeHouseMenuIterator(Iterator):
	def __init__(self, items: dict):
		self.position = 0
		self.items = [item for item in items.values()]

	def has_next(self):
		return self.position < len(self.items)

	def next(self):
		item = self.items[self.position]
		self.position += 1
		return item


class PanCakeHouseMenu:
	def __init__(self):
		self.items = {}

		self.add_item('Шаурма', 'Шаурма по кавказски', False, 190)
		self.add_item('Бургер', 'Бургер грант шеф стронг хрен пор там', False, 560)

	def add_item(self, name, desc, vegetarian, price):
		item = MenuItem(name, desc, vegetarian, price)
		self.items[name] = item

	def create_iterator(self):
		return PanCakeHouseMenuIterator(self.items)


class DinerMenu:
	def __init__(self):
		self.items = []
		self.add_item('Лосось', 'Лосоль халяль', False, 850)
		self.add_item('Салат', 'Салат из травы', True, 8500)

	def add_item(self, name, desc, vegetarian, price):
		item = MenuItem(name, desc, vegetarian, price)
		self.items.append(item)

	def create_iterator(self):
		return DinerMenuIterator(self.items)


class Officiant:
	def __init__(self):
		self.menus = [DinerMenu(), PanCakeHouseMenu()]

	def print_menu(self):
		for i in self.menus:
			iterator = i.create_iterator()
			while iterator.has_next():
				print(iterator.next())


# Инкапсулирован процесс перебора элементов. Для каждой коллекции свой итератор, у которого единые методы перебора
o = Officiant()
o.print_menu()
