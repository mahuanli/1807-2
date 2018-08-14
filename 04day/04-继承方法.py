class Father():
	def __init__(self,name):
		self.name = name
		self.__sfq = 100

	def __play(self):
		print("玩游戏")

	def getsfq(self):
		return self.__sfq

	def getplay(self):
		self.__play()




class Son(Father):
	pass



son = Son("艾斯")

print(son.name)
#print(son.sfq)

#son.play()
print(son.getsfq())
Son.play()


