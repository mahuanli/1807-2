class Son():

	__instance = None
	def __init__(self,name):
		if Son.__flag == False:
			self.name =name
			Son.__flag = True

		self.name = name



	def __new__(cls,*args,**kwargs):
		if cls.__instance = None
			cls.__instance =  super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance





xifu = Son("小明")
print(id(xifu))

xifu1 = Son("王八蛋")
print(id(xifu1))


