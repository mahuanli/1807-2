from socket import *
#创建一个udp的套接字
s = socket(AF_INET,SOCK_DGRAM)
#对方ip 端口
s.bind('',6789)
s.sendto("小仙女".encode("gb2312"),("192.168.43.231",8081))
while True:
	msg = s.recvfrom(1024)
	print("消息是:%S 来自ip:%s"%(msg[0].decode("gb2312"),msg[1][0]))

s.close()
