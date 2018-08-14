class person:
	def eat(self):
		print("吃饭")
	def sleep(self):
		print("睡觉")
	def play(self):
		print("玩")
	def introduce(self):
		print("我的年龄是%d我的身高是%d"%(self.age,self.height))



xiannv = person()
xiannv.eat()
xiannv.sleep()
xiannv.play()
xiannv.age = 18
xiannv.height = 171
xiannv.introduce()
print(xiannv.age)
print(xiannv.height)


ln = person()
ln.eat()
ln.sleep()
ln.play()
ln.age = 18
ln.height = 171










