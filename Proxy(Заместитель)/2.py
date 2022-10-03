from abc import ABC, abstractmethod


class Person(ABC):
	@abstractmethod
	def get_name(self): ...

	@abstractmethod
	def get_gender(self): ...

	@abstractmethod
	def get_geek_rating(self): ...

	@abstractmethod
	def set_name(self, value): ...

	@abstractmethod
	def set_gender(self, value): ...

	@abstractmethod
	def set_geek_rating(self, value): ...


class PersonImpl1(Person):
	def __init__(self):
		self.name = None
		self.gender = None
		self.rating = 0
		self.rating_count = 0

	def get_name(self):
		return self.name

	def get_gender(self):
		return self.gender

	def get_geek_rating(self):
		return 0 if not self.rating_count else self.rating / self.rating_count

	def set_name(self, value):
		self.name = value

	def set_gender(self, value):
		self.gender = value

	def set_geek_rating(self, value):
		self.rating += value
		self.rating_count += 1


class OwnProxy(Person):
	"""
	Реализация заместителя. По сути очень похоже на декоратор. Или на адаптер. Различия можно увидеть только
	в цели паттерна. В данном случае реализован заместитель, который ограничивает доступ к другому экземпляру класса.
	"""
	def __init__(self, person: Person):
		self.person = person

	def get_name(self):
		return self.person.get_name()

	def get_gender(self):
		return self.person.get_gender()

	def get_geek_rating(self):
		return self.person.get_geek_rating()

	def set_name(self, value):
		return self.person.set_name(value)

	def set_gender(self, value):
		return self.person.set_gender(value)

	def set_geek_rating(self, value):
		print('Невозможно присвоить рейтинг себе')


class OtherProxy(Person):
	def __init__(self, person: Person):
		self.person = person

	def get_name(self):
		return self.person.get_name()

	def get_gender(self):
		return self.person.get_gender()

	def get_geek_rating(self):
		return self.person.get_geek_rating()

	def set_name(self, value):
		print('Нет доступа')

	def set_gender(self, value):
		print('Нет доступа')

	def set_geek_rating(self, value):
		return self.person.set_geek_rating(value)


a = PersonImpl1()
i = OwnProxy(a)
other = OtherProxy(a)

a.set_name('Андрей')
a.set_gender('мужик')

print(a.get_name())
print(i.get_name())

i.set_name('Алексей')

print(a.get_name())
print(i.get_name())

other.set_name('сергей')

print(a.get_name())
print(i.get_name())
