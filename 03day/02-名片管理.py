class cardman():
	def __init__(self):
		self.cards = []
	def insert(self):
		d = {}
		name = input("请输入你的名字")
		age = input("请输入你的年龄")
		d["name"] = name
		d["age"] = age
		self.cards
		pass
	def save(self):
		pass
	def find(self):
		pass
	def change(self):
		pass
	def delete(self):
		pass
	def menu(self):
		while true:
			num int(input("请选择功能1,添加2,查看"))
			if num == 1:
				self.insert()
			elif num == 2:
				self.find()
	def save(self):
		with open("data.data","r") as f:
			f.write(str(self.cards))
			if len(f.read()) !=0

			#self.cards = eval(f.read())
				print(eval(f.read()))
cm = carman()
cm.menu()









