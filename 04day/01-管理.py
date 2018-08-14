class dog:
	def __init__(self,name):
		self.name = name
	def getname(self):
		return self.name
	def setname(self,newname):
		if len(newname) >= 4:
			self.name = newname
		else:
			print("error:名字的长度需要大于等于4")

jhiewh = dog("pipi")
print(jhiewh.getname())








