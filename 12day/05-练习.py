from threading import Thread
import time
#多线程对于局部变量不共享
#多线程对于全局变量共享
def work(i):
	num = 0
	time.sleep(i)
	num+=1
	print(num)
'''
def work1(i):
	num = 0
	time.sleep(i)
	num+=2
	print(num)
'''
t = Thread(target=work,args=(3,))
t1 = Thread(target=work,args=(5,))
t.start()

