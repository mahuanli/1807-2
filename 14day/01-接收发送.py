from threading import Thread
from socket import *

s = socket(AF_INET,SOCK_DGRAM)
ip = input("请输入对方ip:")
port = int(input("请输入端口:"))
s.bind(("",8888))


def send():
	while True:
		msg = input("请输入发送内容")
		s.sendto(msg.encode("gb2312"),(ip,port))

def recv():
	while True():
		msg = s.recvfrom(1024)
		print("\r接到消息:%s"%msg[0].decode("gb2312"))

t1 = Thread(target= send)
t2 = Thread(target=recv)
t1.start()
t2.start()
t1.join()
t2.join()


