class Car():
	def __init__(self,color):
		self.color = color

	def run(self):
		print("-----run-------")


class Bmw(Car):
	def __init__(self,color):
		self.count = 6
		super().__init__(color)

	def run(self):
		print("bmw--run")


class BenChi(Car):
	def run(self):
		print("benchi--run")


class Bieke(Car):
	def run(self):
		print("biekr==run")



class birke(Car):
	def run(self):
		print(bieke==run)


class Factory():
	def create(self):
		pass



