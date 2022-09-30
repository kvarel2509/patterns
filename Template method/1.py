class Coffee:
	def boiling_water(self):
		print('Boiling water')

	def brew_coffee_grinds(self):
		print('Dripping coffee through filter')

	def pour_in_cap(self):
		print('Pouring into cup')

	def add_sugar_and_milk(self):
		print('Adding sugar and milk')

	def prepare_recipe(self):
		self.boiling_water()
		self.brew_coffee_grinds()
		self.pour_in_cap()
		self.add_sugar_and_milk()


class Tea:
	def boiling_water(self):
		print('Boiling water')

	def steep_tea_bag(self):
		print('Steeping the tea')

	def add_lemon(self):
		print('Adding lemon')

	def pour_in_cup(self):
		print('Pouring into cup')

	def prepare_recipe(self):
		self.boiling_water()
		self.steep_tea_bag()
		self.add_lemon()
		self.pour_in_cup()
