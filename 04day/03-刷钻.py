class QQ():


	def __openvip(self):
		print("会员开通成功")


	def checkqq(self,money):
		if money > 10:
			self.__openvip()


		else:
			print("不能开通")



qq =  QQ()
qq.checkqq(12)



qq1 = QQ()
qq1.checkqq(10)
