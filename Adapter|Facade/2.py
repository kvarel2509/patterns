class ListPist:
	def __init__(self):
		self.obj = list()

	def __str__(self):
		return f"[{' потом '.join([str(i) for i in self.obj])}]"

	def добавь_я_сказал(self, item):
		self.obj.append(item)
		print(self)

	def удалить_нахер(self, item):
		self.obj.remove(item)
		print(self)


a = ListPist()
a.добавь_я_сказал(5)
a.добавь_я_сказал(3)
a.удалить_нахер(3)
