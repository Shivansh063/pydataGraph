#!/usr/bin/env python2

import  socket
import matplotlib.pyplot as plt 


#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
#ip="192.168.1.4"
port=7890
#  binind ip and port with bind function that takes input as tuple
s.bind(("",port))

# defining  empty list 
x={}
for  z in range(10) :
#  now receiving data
	data=s.recvfrom(100)
	print  "only data :  ",data[0]
	x[data[0]] = x.get(data[0],0)+1

r = x.items()
a,b=zip(*r)
#labeling and creating graph by above two tuples
plt.xlabel("messages received")
plt.ylabel("number of occurance")
plt.scatter(a,b,label="dot plot",s=200)
plt.plot(a,b,label="line plot")
plt.bar(a,b,label="bar plot",color='green')
plt.legend()
plt.grid()
plt.show()
s.close()



