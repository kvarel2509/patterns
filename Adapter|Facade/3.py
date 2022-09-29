class Facade:
	def __init__(self, class1, class2, class3, class4, class5):
		self.class1 = class1
		self.class2 = class2
		self.class3 = class3
		self.class4 = class4
		self.class5 = class5

	def fast_method1(self):
		return self.class1 + self.class2

	def fast_method2(self):
		self.class1
		self.class3
		self.class5

