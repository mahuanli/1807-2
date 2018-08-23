from multiprocessing import Pool,Manger
import time
def writer(q):
	for i in 'laowang':
		q.put(i)
		print('写入队列成功')
		time.sleep(1)
def reader(q):
	while True:
		if not q.empty():
			msg = q.get()
			print(msg)
			if msg =='g':
				break
			time.sleep(1)
p = Pool(3)
q = Manager().Queue()
p.apply_async(writer,(q,))
p.apply_async(reader,(q,))
