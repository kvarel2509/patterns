import time
from abc import ABC, abstractmethod
import random
from operator import add, sub
import string


# Игра, для реализации которой использованы несколько паттернов проектирования.


class Game(ABC):
	"""
	Класс является абстрактным и реализует паттерн "ШАБЛОННЫЙ МЕТОД". Сам метод описан в run().
	При наследовании от этого класса необходимо обязательно реализовать метод description() и process()
	Так же в методе расставлены хуки, которые можно определить в дочернем классе.
	"""
	@abstractmethod
	def process(self): ...

	@abstractmethod
	def description(self): ...

	def hook1(self): ...

	def hook2(self): ...

	def hook3(self): ...

	def run(self):
		self.hook1()
		print('*' * 30)
		print(f'''
		{self.description()}
		Для начала игры нажмите кнопку "ENTER"
		''')
		print('*' * 30)
		self.hook2()
		input()
		result = self.process()
		self.hook3()
		time.sleep(3)
		return result


class GameDecorator(Game, ABC):
	"""
	Абстрактный класс, отвечает за декорирование игры. Схема паттерна "ДЕКОРАТОР"
	"""
	def __init__(self, game: Game):
		self.game = game

	@abstractmethod
	def description(self): ...


class TimeGameDecorator(GameDecorator):
	"""
	Реализация паттерна "ДЕКОРАТОР". Сохраняется ссылка на игру. И вызов метода в классе игры декорируются
	дополнительной логикой
	"""
	def __init__(self, game: Game, period=10):
		super().__init__(game)
		self.period = period

	def description(self):
		return f"""{self.game.description()}
		Обратите внимание, у этого задания есть ограничение по времени - {self.period} секунд"""

	def process(self):
		time_start = time.perf_counter()
		result_game = self.game.process()
		time_delta = time.perf_counter() - time_start
		if result_game:
			print(f'Вы выполнили задание за {round(time_delta, 2)} секунд')
			print(f'Вы {"" if time_delta < self.period else "не "}уложились во время')

		return result_game and time_delta < self.period


class CalculationGame(Game):
	def description(self):
		return 'Игра "Вычисления". Вам необходимо правильно решить пример.'

	def process(self):
		x, y = [random.randint(100, 999) for _ in range(2)]
		operation = random.choice([add, sub])
		right = operation(x, y)
		user_response = input(f'Сколько будет {str(x)} {"+" if operation == add else "-"} {str(y)}: ')

		try:
			result = int(user_response) == right
			print(f'Правильный ответ: {str(right)}. Вы ответили {"правильно" if result else "неправильно"}')
			return result
		except ValueError:
			pass
		return False


class ReprintGame(Game):
	def description(self):
		return '''Игра "Перепечатай без ошибок". Вам необходимо правильно перепечатать предложенный текст.'''

	def process(self):
		len_text = 20
		right = ''.join(random.choices(string.printable, k=len_text))
		print(f'Перепечатайте следующий фрагмент:')
		print(right)
		user_response = input('Ответ: ')
		result = user_response == right
		print(f'Вы ответили {"ПРАВИЛЬНО" if result else "НЕПРАВИЛЬНО"}')
		return result


class CoincidenceGame(Game):
	def description(self):
		return '''Игра "Найди количество совпадений". Вам необходимо посчитать,
сколько раз встречается указанный символ в последовательности'''

	def process(self):
		target, other = random.choice([('Q', 'O'), ('O', 'Q'), ('P', 'R'), ('R', 'P'), ('W', 'V'), ('V', 'W')])
		len_sequence = 50
		sequence = ''.join(random.choices([target, other], k=len_sequence))
		right = sequence.count(target)
		print(f'Сколько раз встречается буква {target} в последовательности:')
		print(sequence)
		user_response = input('Ответ: ')

		try:
			result = int(user_response) == right
			print(f'Правильный ответ: {str(right)}. Вы ответили {"правильно" if result else "неправильно"}')
			return result
		except ValueError:
			pass
		return False


class State(ABC):
	"""
	Класс является абстрактным и по факту реализуется 2 паттерна. "ШАБЛОННЫЙ МЕТОД" run(), а так же класс является
	частью паттерна "СОСТОЯНИЕ".
	"""
	DESC: str

	def run(self):
		direction = '0'
		print('*' * 30)
		print(f'\t\t{self.DESC}')
		print('*' * 30)
		print()
		input()
		while direction not in ['1', '2', '3']:
			direction = input('Выбери направление. 1 - направо, 2 - налево, 3 - прямо: ')
			time.sleep(3)
			if direction == '1':
				self.right()
			elif direction == '2':
				self.left()
			elif direction == '3':
				self.center()

	@abstractmethod
	def left(self): ...

	@abstractmethod
	def right(self): ...

	@abstractmethod
	def center(self): ...


class Point1(State):
	"""
	Реализация паттерна "СОСТОЯНИЕ". Представляет реализацию конкретного состояния.
	Сохраняет в себе экземпляр класса GameControl, далее в своих методах left(), right(), center() запускает
	изменение состояния в этом атрибуте. В данном случае есть отступление, так как класс не знает,
	с какими состояниями системы он контактирует. Допускается, что класс будет знать, какое конкретное
	состояние он может вызвать. В этом случае должен использоваться метод например set_state()
	"""
	DESC = '1 уровень'

	def __init__(self, game_control: 'GameControl', game: Game):
		self.game_control = game_control
		self.game = game

	def left(self):
		game_result = self.game.run()
		if game_result:
			self.game_control.up_state()
		else:
			self.game_control.down_state()

	def right(self):
		print('Тебе повезло, ты переходишь на следующий уровень')
		self.game_control.up_state()

	def center(self):
		print('Тебе повезло, ты переходишь на следующий уровень')
		self.game_control.up_state()


class Point2(State):
	DESC = '2 уровень'

	def __init__(self, game_control: 'GameControl', game: Game):
		self.game_control = game_control
		self.game = game

	def left(self):
		game_result = self.game.run()
		if game_result:
			self.game_control.up_state()
		else:
			self.game_control.down_state()

	def right(self):
		game_result = self.game.run()
		if game_result:
			self.game_control.up_state()
		else:
			self.game_control.down_state()

	def center(self):
		print('К сожалению, ты спускаешься на уровень ниже')
		self.game_control.down_state()


class Point3(State):
	DESC = '3 уровень'

	def __init__(self, game_control: 'GameControl', game: Game):
		self.game_control = game_control
		self.game = game

	def left(self):
		game_result = self.game.run()
		if game_result:
			self.game_control.up_state()
		else:
			self.game_control.down_state()

	def right(self):
		game_result = self.game.run()
		if game_result:
			self.game_control.up_state()
		else:
			self.game_control.down_state()

	def center(self):
		game_result = self.game.run()
		if game_result:
			self.game_control.up_state()
		else:
			self.game_control.down_state()


class GameControl:
	"""
	Класс управляет состояниями системы. В данной реализации self.points представляет собой список всех уровней.
	Есть смысл номера уровней вынести из класса. Тогда в момент инициализации класса можно выстроить порядок следования
	уровней и их реализация. Исполнение методов left(), center(), right() делегируется конкретному состоянию.

	Отличительная разница паттернов СОСТОЯНИЕ и СТРАТЕГИЯ в том, что каждое состояние, оно же стратегия, имеет
	возможность обратиться к базовому классу и подменить себя другой стратегией, оно же состояние.

	В паттерне СТРАТЕГИЯ как правило клиент определяет стратегию исполнения. В паттерне СОСТОЯНИЕ это делает
	либо само состояние, либо контекст, но не клиент.
	"""
	def __init__(self):
		self.points = [Point1(self, TimeGameDecorator(CalculationGame(), 10)), Point2(self, ReprintGame()), Point3(self, CoincidenceGame())]
		self.state = 0

	def up_state(self):
		self.state += 1

		if self.state >= len(self.points):
			print('Поздравляем! Ты победил! Игра окончена')
		else:
			self.points[self.state].run()

	def down_state(self):
		self.state -= 1
		if self.state < 0:
			print('К сожалению, ты проиграл! Игра окончена')
		else:
			self.points[self.state].run()

	def left(self):
		return self.points[self.state].left()

	def center(self):
		return self.points[self.state].center()

	def right(self):
		return self.points[self.state].right()

	def play(self):
		print('''
		Привет. Перед тобой игра. Чтобы ее пройти, нужно выполнять задания и подниматься по уровням.
		В игре 3 уровня. На каждом тебе будет предложено выбрать направление движения. Игра либо:
		- переведет тебя сразу на уровень выше,
		- предложит пройти задание. Если получится, ты перейдешь на следующий уровень, иначе опустишься на предыдущий
		- переведет тебя на уровень ниже.
		Если ты опустишься ниже 1 уровня, ты проиграла, если прошла 3 уровень - победила.
		Давай уже начнем!!!
*************************************************************************************************************
''')
		input()
		return self.points[self.state].run()


a = GameControl()
a.play()
