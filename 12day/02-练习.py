from multiprocessing import Pool
import time

def show():
	for i in range(10):
		time.sleep(1)
		print("哈哈哈哈")

p = Pool()
for i in range(3):
	p.apply_async(show)



	print("添加成功")
p.close()
p.join()
print("哦哦哦哦哦哦")
