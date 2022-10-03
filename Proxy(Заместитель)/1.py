import time
from abc import ABC, abstractmethod


class Text(ABC):
	@abstractmethod
	def get_text(self): ...


class StrongText(Text):
	def get_text(self):
		time.sleep(10)
		return 'QWERTY'


class ProxyStrongText(Text):
	def __init__(self, strong_text: StrongText):
		self.strong_text = strong_text

	def get_text(self):
		print('Ожидаем формирование текста')
		return self.strong_text.get_text()


a = StrongText()
b = ProxyStrongText(a)
print(b.get_text())
