from threading import Thread
import time

num = 0
flag = 1
def work1():
	global num,flag
	if flag == 1:
		for i in range(10000000):
			num+=1
		print('thread-1')
		print(num)
		flag = 2
def work2():
	global num
	while True:
		if flag == 2:
			for i in range(1000000):
				num+=1



