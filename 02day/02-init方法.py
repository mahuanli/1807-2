class dog():

	def __init__(self,name,age):#实例化方法 默认被调用

		self.name = name
		self.age = age

		#print("被调用了")
		


	def wark(self):
		print("汪汪叫")

	def eat(self):
		print("吃狗粮")



hashiqi = dog("三哈",10)#创建对象或创建一个实例
hashiqi.wark()
hashiqi.eat()

#hashiqi.age = 10
#hashiqi.name = "哈士奇"
print(hashiqi.age)
print(hashiqi.name)




























