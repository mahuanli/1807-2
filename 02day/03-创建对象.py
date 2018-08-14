class car():
	def __init__(self,color,type):
		#self.name = name
		self.color= color
		self.type = type
	def __str__(self):
		a = "颜色是%s,型号是%s"%(self.color,self.type)
		return a
	def move(self):
		print("车跑")

	def music(self):
		print("切音乐")



mashaladi = car("红色","mashaladi8")
mashaladi.move()
mashaladi.music()
print(mashaladi)

#mashaladi.color = "红色"




