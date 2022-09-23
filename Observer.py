from abc import ABC, abstractmethod

# class WeatherStation: ...
#
#
# class CurrentStateDisplay:
# 	def display(self): ...
# 	def update(self): ...
#
#
# class StatisticDisplay:
# 	def display(self): ...
# 	def update(self): ...
#
#
# class ForecastDisplay:
# 	def display(self): ...
# 	def update(self): ...
#
#
# class WeatherData:
# 	def get_temperature(self): ...  # температура
#
# 	def get_humidity(self): ...  # влажность
#
# 	def get_pressure(self): ...  # атмосферное давление
#
# 	def measurements_changed(self):
# 		temp = self.get_temperature()
# 		humidity = self.get_humidity()
# 		pressure = self.get_pressure()
#
# 		CurrentStateDisplay.update()
# 		StatisticDisplay.update()
# 		ForecastDisplay.update()

# Нельзя добавить новый экран, так как они жестко указаны. Придется править этот класс при каждом изменении
# Нужно стремиться к слабой связанности объектов. Чем меньше они знают о чужой реализации, тем лучше

# _______________________________________________________________________________________________________


class Subject(ABC):
	"""
	Здесь можно было бы реализовать функционал, но тогда теряется возможность переиспользовать класс везде.
	Например - Один субъект просто оповещает других, другой шлет еще какие-то данные. Третий имеет ограничения по
	количеству наблюдателей. и т.д.
	"""

	@abstractmethod
	def register_observer(self, observer):
		pass

	@abstractmethod
	def remove_observer(self, observer):
		pass

	@abstractmethod
	def notify_observers(self, *args, **kwargs):
		pass


class Observer(ABC):
	@abstractmethod
	def update(self, *args, **kwargs):
		pass


class Display(ABC):
	@abstractmethod
	def display(self):
		pass


class WeatherData(Subject):
	def __init__(self):
		self.observers = []
		self.__temperature = None
		self.__humidity = None
		self.__pressure = None

	def register_observer(self, observer):
		self.observers.append(observer)

	def remove_observer(self, observer):
		self.observers.remove(observer)

	def notify_observers(self):
		[observer.update() for observer in self.observers]

	def measurements_changed(self):
		self.notify_observers()

	def set_measurements(self, temperature, humidity, pressure):
		self.__temperature = temperature
		self.__humidity = humidity
		self.__pressure = pressure
		self.measurements_changed()

	@property
	def temperature(self):
		return self.__temperature

	@property
	def humidity(self):
		return self.__humidity

	@property
	def pressure(self):
		return self.__pressure


class CurrentDisplay(Observer, Display):
	def __init__(self, subject: WeatherData):
		self.subject = subject
		self.subject.register_observer(self)
		self.temperature = None
		self.humidity = None
		self.pressure = None

	def update(self, *args, **kwargs):
		self.temperature = self.subject.temperature
		self.humidity = self.subject.humidity
		self.pressure = self.subject.pressure
		self.display()

	def display(self):
		print(f'{self.temperature} / {self.humidity} / {self.pressure}')


class SumDisplay(Observer, Display):
	def __init__(self, subject: WeatherData):
		self.subject = subject
		self.subject.register_observer(self)
		self.sum = None

	def update(self, *args, **kwargs):
		self.sum = sum([self.subject.temperature, self.subject.pressure, self.subject.humidity])
		self.display()

	def display(self):
		print(f'Сумма - {self.sum}')


class WeatherStation:
	def __init__(self):
		a = WeatherData()
		CurrentDisplay(a)
		SumDisplay(a)
		a.set_measurements(30, 40, 50)
		a.set_measurements(50, 60, 90)


WeatherStation()

# В питоне можно задать удобные параметры *args и *kwargs, которых вроде нет в TS. Но это не точно.
# Их повесить на update

# Нужно стремиться к слабой связанности объектов. Теперь Субъект не знает, кого оповещает.
# У него есть публичное API, в котором прописано, какие методы есть. И наблюдатель их забирает.
