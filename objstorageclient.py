#!/usr/bin/env python2

import  socket
import  time
import  commands
import  os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_ip="192.168.1.81"
port=8888

d_name=raw_input("enter drive name :  ")
d_size=raw_input("enter drive size in MB :  ")
s.sendto(d_name,(server_ip,port))
s.sendto(d_size,(server_ip,port))

print  "Plz wait for server  responce"
time.sleep(5)
os.system('mkdir  /media/'+d_name)
os.system('mount  '+server_ip+':/mnt/'+d_name+'  /media/'+d_name)


