from abc import ABC


class MenuComponent(ABC):
	def add(self, menu_component):
		raise NotImplementedError()

	def remove(self, menu_component):
		raise NotImplementedError()

	def get_child(self, i):
		raise NotImplementedError()

	def get_name(self):
		raise NotImplementedError()

	def get_price(self):
		raise NotImplementedError()


class MenuItem(MenuComponent):
	def __init__(self, name, price):
		self.__name = name
		self.__price = price

	def get_name(self):
		return self.__name

	def get_price(self):
		return self.__price

	def __str__(self):
		return f'{self.get_name()} - {self.get_price()}'


class Menu(MenuComponent):
	def __init__(self, name):
		self.__name = name
		self.__menu = []

	def add(self, menu_component):
		self.__menu.append(menu_component)

	def remove(self, menu_component):
		self.__menu.remove(menu_component)

	def get_child(self, i):
		return self.__menu[i]

	def __str__(self):
		text = f'{self.__name} \n'
		text += '-' * 20 + '\n'
		for item in self.__menu:
			text += '\t' + str(item) + '\n'
		return text


class Waitress:
	def __init__(self, menu):
		self.__menu = menu

	def print_menu(self):
		print(self.__menu)


menu = Menu('all manu')
diner = Menu('diner menu')
breakfast = Menu('breakfast menu')
dessert = Menu('dessert')
diner.add(MenuItem('lapsha', 1500))
diner.add(dessert)
diner.add(MenuItem('shaverma', 190))
dessert.add(MenuItem('pirog', 300))
dessert.add(MenuItem('cake', 100))
breakfast.add(MenuItem('egg', 30))
breakfast.add(MenuItem('coffee', 200))
menu.add(diner)
menu.add(breakfast)

off = Waitress(menu)
off.print_menu()
