from abc import ABC, abstractmethod
from typing import Optional


class Command(ABC):
	@abstractmethod
	def on(self): ...

	@abstractmethod
	def off(self): ...


class Light:
	def light_on(self):
		return 'Light ON'

	def light_off(self):
		return 'Light OFF'


class Shower:
	def shower_on(self):
		return 'Shower ON'

	def shower_off(self):
		return 'Shower OFF'


class GarageDoor:
	def up(self):
		return 'Garage OPEN'

	def down(self):
		return 'Garage CLOSES'


# У объектов разные интерфейсы


class LightCommand(Command):
	def __init__(self, light):
		self.light = light

	def on(self):
		return self.light.light_on()

	def off(self):
		return self.light.light_off()


class GarageDoorCommand(Command):
	def __init__(self, obj):
		self.obj: GarageDoor = obj

	def on(self):
		return self.obj.up()

	def off(self):
		return self.obj.down()


class ShowerCommand(Command):
	def __init__(self, obj):
		self.obj: Shower = obj

	def on(self):
		return self.obj.shower_on()

	def off(self):
		return self.obj.shower_off()


class NoCommand(Command):
	def on(self):
		return 'Команда не назначена'

	def off(self):
		return 'Команда не назначена'


class SimpleRemoteController:

	def __init__(self, size: int):
		self.size = size
		self.slots_on = [NoCommand().on for _ in range(size)]
		self.slots_off = [NoCommand().off for _ in range(size)]

	def set_command(self, position: int, command: Command):
		self.slots_on[position] = command.on
		self.slots_off[position] = command.off  # здесь сохраняем ссылки на функции, не вызываем их

	def on(self, position: int):
		return self.slots_on[position]()

	def off(self, position: int):
		return self.slots_off[position]()

	def show_panel(self):
		[
			print(f'{row_slots} ряд \t {self.on(row_slots)} \t {self.off(row_slots)}')
			for row_slots in range(self.size)
		]


# Видимо не всегда имеется смысл хранить сразу несколько операций в одной команде
l = Light()
s = Shower()
d = GarageDoor()
lc = LightCommand(l)
sc = ShowerCommand(s)
dc = GarageDoorCommand(d)
remote = SimpleRemoteController(7)
remote.set_command(1, lc)
remote.set_command(3, sc)
remote.set_command(6, dc)
remote.show_panel()
print(remote.on(2))

# Внутри команд можно хранить состояние.
