from abc import ABC, abstractmethod


# class Duck(ABC):
# 	SUFFIX = 'duck'
#
# 	def quack(self):
# 		print(f'{self.SUFFIX}: Кря')
#
# 	def swim(self):
# 		print(f'{self.SUFFIX}: Буль буль')
#
# 	def fly(self):
# 		print(f'{self.SUFFIX}: Лечу')
#
# 	@abstractmethod
# 	def display(self):
# 		pass
#
#
# class MallardDuck(Duck):
# 	SUFFIX = 'mallard duck'
#
# 	def display(self):
# 		print(f'i am {self.SUFFIX}')
#
# 	def fly(self):
# 		print(f'{self.SUFFIX}: я не летаю')
#
#
# class RedheadDuck(Duck):
# 	SUFFIX = 'redhead duck'
#
# 	def fly(self):
# 		print(f'{self.SUFFIX}: я не летаю')
#
# 	def swim(self):
# 		print(f'{self.SUFFIX}: я не Буль буль')
#
# 	def display(self):
# 		print(f'i am {self.SUFFIX}')
#
#
# class RubberDuck(Duck):
# 	SUFFIX = 'rubber duck'
#
# 	def display(self):
# 		print(f'i am {self.SUFFIX}')
#
# 	def fly(self):
# 		print(f'{self.SUFFIX}: я не летаю')
#
#
# class DecoyDuck(Duck):
# 	SUFFIX = 'decoy duck'
#
# 	def display(self):
# 		print(f'i am {self.SUFFIX}')
#
# 	def quack(self):
# 		print(f'{self.SUFFIX}: Я не Кря')
#
# 	def swim(self):
# 		print(f'{self.SUFFIX}: Я не Буль буль')
#
# 	def fly(self):
# 		print(f'{self.SUFFIX}: Я не летаю')

# ------------------------------------------------------------------------------------------

# class Duck(ABC):
# 	SUFFIX = 'duck'
#
# 	@abstractmethod
# 	def display(self):
# 		pass


# class Quackable(ABC):
# 	@abstractmethod
# 	def quack(self):
# 		pass
#
#
# class RedheadDuck(Duck, Quackable):
# 	def quack(self):
# 		print(f'{self.SUFFIX}: Я крякаю')
#
# 	def display(self):
# 		print(f'i am {self.SUFFIX}')

# ___________________________________________________________________________________


# class Flyable:
# 	def fly(self):
# 		print(f'{self.SUFFIX}: Я летаю')
#
#
# class NoFlyable:
# 	def fly(self):
# 		print(f'{self.SUFFIX}: Я не летаю')
#
#
# class Swimable:
# 	def swim(self):
# 		print(f'{self.SUFFIX}: Я плаваю')
#
#
# class NoSwimable:
# 	def swim(self):
# 		print(f'{self.SUFFIX}: Я не плаваю')
#
#
# class RedheadDuck(Duck, NoFlyable, NoSwimable):
# 	SUFFIX = 'redhead duck'
#
# 	def display(self):
# 		print(f'i am {self.SUFFIX}')

# Такой вариант уже хорош, но нельзя динамично изменить поведение. Например: охота на уток. Утка умеет летать. Но
# если сломается крыло или она будет подбита, поведение поменять не получится

# _________________________________________________________________________________________________________

class FlyBehavior(ABC):
	@abstractmethod
	def fly(self): ...


class SwimBehavior(ABC):
	@abstractmethod
	def swim(self): ...


class FlyWithWings(FlyBehavior):
	def fly(self):
		print(f'я умею летать')


class FlyNoWay(FlyBehavior):
	def fly(self):
		print(f'я не умею летать')


class SwimYes(SwimBehavior):
	def swim(self):
		print(f'я умею плавать')


class SwimNoWay(SwimBehavior):
	def swim(self):
		print(f'я не умею плавать')


class Duck(ABC):
	SUFFIX = 'duck'
	fly_behavior: FlyBehavior
	swim_behavior: SwimBehavior

	def fly(self):
		return self.fly_behavior.fly()

	def swim(self):
		return self.swim_behavior.swim()

	def set_fly_behavior(self, fly_behavior):
		self.fly_behavior = fly_behavior()

	def set_swim_behavior(self, swim_behavior):
		self.swim_behavior = swim_behavior()


class MallardDuck(Duck):
	fly_behavior = FlyWithWings()
	swim_behavior = SwimNoWay()


class DuckSimulator:
	def __init__(self):
		a = MallardDuck()
		a.fly()
		a.swim()
		a.set_swim_behavior(SwimYes)
		a.swim()


DuckSimulator()

# Заменяем понятие "ЯВЛЯЕТСЯ" на "СОДЕРЖИТ". Такие системы более гибкие.
# Наследование предполагает закрепление поведения. Композиция позволяет менять поведение динамически
# Нужно инкапсулировать то, что может поменяться.
# Нужно программировать на уровне СУПЕРКЛАССОВ. И использовать в реализации те методы, которые в них реализованы
