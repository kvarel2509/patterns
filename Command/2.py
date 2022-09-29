from abc import ABC, abstractmethod


class Command(ABC):
	@abstractmethod
	def execute(self): ...

	@abstractmethod
	def undo(self): ...


class Light:
	def light_on(self):
		return 'Light ON'

	def light_off(self):
		return 'Light OFF'


class CeilingFan:
	NULL = 0
	LOW = 1
	MIDDLE = 2

	def __init__(self):
		self.speed = self.NULL

	def set_speed(self, speed):
		self.speed = speed

		if self.speed == 0:
			return 'CeilingFan OFF'
		elif self.speed == 1:
			return 'CeilingFan ON speed LOW'
		elif self.speed == 2:
			return 'CeilingFan ON speed MIDDLE'

	def get_state(self):
		return f'CeilingFan have speed {self.speed}'


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


class LightOnCommand(Command):
	def __init__(self, obj: Light):
		self.obj = obj

	def execute(self):
		return self.obj.light_on()

	def undo(self):
		return self.obj.light_off()

	def __str__(self):
		return 'Light On'


class LightOffCommand(Command):
	def __init__(self, obj: Light):
		self.obj = obj

	def execute(self):
		return self.obj.light_off()

	def undo(self):
		return self.obj.light_on()

	def __str__(self):
		return 'Light off'


class CeilingFanOnLowCommand(Command):
	def __init__(self, obj: CeilingFan):
		self.obj = obj
		self.state = None

	def execute(self):
		self.state = self.obj.speed
		return self.obj.set_speed(1)

	def undo(self):
		return self.obj.set_speed(self.state)

	def __str__(self):
		return 'Ceiling fan on low'


class CeilingFanOnMiddleCommand(Command):
	def __init__(self, obj: CeilingFan):
		self.obj = obj
		self.state = None

	def execute(self):
		self.state = self.obj.speed
		return self.obj.set_speed(2)

	def undo(self):
		return self.obj.set_speed(self.state)

	def __str__(self):
		return 'Ceiling fan on middle'


class CeilingFanOffCommand(Command):
	def __init__(self, obj: CeilingFan):
		self.obj = obj
		self.state = None

	def execute(self):
		self.state = self.obj.speed
		return self.obj.set_speed(0)

	def undo(self):
		return self.obj.set_speed(self.state)

	def __str__(self):
		return 'Ceiling fan off'


class MarcoCommand(Command):
	def __init__(self, *args: Command):
		self.objs = args

	def execute(self):
		return [obj.execute() for obj in self.objs]

	def undo(self):
		return [obj.undo() for obj in self.objs]

	def __str__(self):
		return ', '.join([str(command) for command in self.objs])


class NoCommand(Command):
	def execute(self):
		return 'Команда не назначена'

	def undo(self):
		return self.execute()

	def __str__(self):
		return 'No command'


class RemoteCommand:
	def __init__(self, size: int):
		self.size = size
		self.commands_on = [NoCommand() for _ in range(self.size)]
		self.commands_off = [NoCommand() for _ in range(self.size)]
		self.history = []

	def set_command(self, row: int, command_on: Command, command_off: Command):
		self.commands_on[row] = command_on
		self.commands_off[row] = command_off

	def click_on(self, row: int):
		self.history.append(self.commands_on[row])
		return self.commands_on[row].execute()

	def click_off(self, row: int):
		self.history.append(self.commands_off[row])
		return self.commands_off[row].execute()

	def undo(self):
		if not self.history:
			return 'Нет команд для отмены'

		command = self.history.pop()
		return command.undo()

	def show_menu(self):
		[
			print(f'ряд №{row} \t {self.commands_on[row]} \t {self.commands_off[row]}')
			for row in range(self.size)
		]

l = Light()
c = CeilingFan()
lc_on = LightOnCommand(l)
lc_off = LightOffCommand(l)
cc_on_low = CeilingFanOnLowCommand(c)
cc_on_middle = CeilingFanOnMiddleCommand(c)
cc_off = CeilingFanOffCommand(c)
mc_on = MarcoCommand(lc_on, cc_on_middle)
mc_off = MarcoCommand(lc_off, cc_off)

remote = RemoteCommand(5)
remote.set_command(0, lc_on, lc_off)
remote.set_command(2, cc_on_low, cc_off)
remote.set_command(3, cc_on_middle, cc_off)
remote.set_command(4, mc_on, mc_off)
remote.show_menu()

# print(c.get_state())
print(remote.click_on(2))
# print(c.get_state())
print(remote.undo())
# print(c.get_state())
print(remote.click_on(4))
# print(c.get_state())
print(remote.click_off(4))
# print(c.get_state())

# Паттерн команда позволяет исполнять запрос в любое время, даже намного позже его объявления. Так же паттерн
# позволяет сохранять список выполненных операций, с возможностью реализации транзакций, отмены действий и прочее...
