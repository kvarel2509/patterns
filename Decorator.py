from abc import ABC, abstractmethod


# class Beverage(ABC):
# 	DESCRIPTION: str
#
# 	def get_description(self) -> str:
# 		return self.DESCRIPTION
#
# 	@abstractmethod
# 	def cost(self) -> float:
# 		pass
#
#
# class HouseBlend(Beverage):
# 	DESCRIPTION = 'House Blend'
#
# 	def cost(self):
# 		return 1.99
#
#
# class Espresso(Beverage):
# 	DESCRIPTION = 'Espresso'
#
# 	def cost(self) -> float:
# 		return 2.09


# class HouseBlendAndMocha(Beverage):
# 	DESCRIPTION = 'House Blend and Mocha'
#
# 	def cost(self) -> float:
# 		return 2.49

# Таким образом у нас множатся классы. Существует несколько дополнений к основному классу. Их можно комбинировать.
# Нарушаются принципы проектирования: Изменения не инкапсулируются.
# Если стоимость компонента изменится, придется вносить много изменений. В классах наблюдается привязка к реализации.
# Есть вариант решать этот вопрос в базовом классе:

# ___________________________________________________________________________________________________________
# class Beverage(ABC):
# 	DESCRIPTION: str
# 	MILK = False
# 	SOY = False
# 	MOCHA = False
# 	WHIP = False
#
# 	def get_description(self) -> str:
# 		return self.DESCRIPTION
#
# 	def cost(self) -> float:
# 		cost = 0
# 		if self.has_milk():
# 			cost += 0.17
# 		if self.has_soy():
# 			cost += 0.19
# 		if self.has_mocha():
# 			cost += 0.49
# 		if self.has_whip():
# 			cost += 0.79
# 		return cost
#
# 	def has_milk(self):
# 		return bool(self.MILK)
#
# 	def has_soy(self):
# 		return bool(self.SOY)
#
# 	def has_mocha(self):
# 		return bool(self.MOCHA)
#
# 	def has_whip(self):
# 		return bool(self.WHIP)
#
# 	def set_milk(self, value: bool):
# 		self.MILK = value
#
# 	def set_soy(self, value: bool):
# 		self.SOY = value
#
# 	def set_mocha(self, value: bool):
# 		self.MOCHA = value
#
# 	def set_whip(self, value: bool):
# 		self.WHIP = value
#
#
# class HouseBlend(Beverage):
# 	DESCRIPTION = 'House Blend'
#
# 	def cost(self) -> float:
# 		return 1.99 + super().cost()


# Такой подход помогает избавиться от кучи дочерних классов. Но есть недостатки:
# - При любом изменении придется вносить изменения в базовый класс
# - Все дочерние классы наследуют все методы, даже если они неуместны
# - Сложная логика расчета необычных добавок. Например, двойная порция MILK не просчитывается корректно.

# ___________________________________________________________________________________________________________

class Beverage(ABC):
	DESCRIPTION: str

	def get_description(self):
		return self.DESCRIPTION

	@abstractmethod
	def cost(self) -> float: ...


class HouseBlend(Beverage):
	DESCRIPTION = 'House blend'

	def cost(self) -> float:
		return 1.99


class BeverageDecorator(Beverage):
	def __init__(self, beverage):
		self.beverage = beverage

	@abstractmethod
	def get_description(self): ...


class Milk(BeverageDecorator):
	DESCRIPTION = 'Молоко'

	def get_description(self):
		return f'{self.beverage.get_description()}, {self.DESCRIPTION}'

	def cost(self) -> float:
		return self.beverage.cost() + 0.49


class Mocha(BeverageDecorator):
	DESCRIPTION = 'Мокко'

	def get_description(self):
		return f'{self.beverage.get_description()}, {self.DESCRIPTION}'

	def cost(self) -> float:
		return self.beverage.cost() + 0.99


# На первый взгляд, расчет стоимости очевиден. Его можно вынести выше. Но стоит реально подумать, может ли меняться
# какой-либо участок кода. И очень осторожно прописывать реализацию на высоком уровне абстракции.
# Вместо этого можно рассмотреть вариант инкапсуляции по паттерну Стратегия.
# В этом примере я вынес поле PRICE. Теперь оно задается статически. Нет гибкости определения базовой цены.
# Вдруг обращается постоянный клиент? Вдруг проходит акция? Тут мы можем изменить расчет в методы cost.
# Но вдруг появляется несколько базовых цен, которые зависят от размера напитка?

