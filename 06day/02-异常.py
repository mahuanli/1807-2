class showError(Exception):
	def __init__(self,name):
		self.name = name

class InputManger():
	def my_input(self):
		self.name = input("请输入你的名字")


		try:
			if self.name == "老王":
				raise showError(self.name)
		except showError as ret:
			print("输入%s就报错"%ret.name)


im = InputManger()
im.my_input()








