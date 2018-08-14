class car():
	def __init__(self,newwheelnum,newcolor):
		self.wheelnum = newwheelnum
		self.color = newcolor


	def move(self):
		print('车在跑，目标：澳门')

msld = car(5,'read')
print('车的颜色为:%s'%msld.color)
print('车轮胎的数量:%s'%msld.wheelnum)

print('内存地址:',id(msld))
