#!/usr/bin/env python2

import  socket
import  time
import  commands
import  os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_ip="192.168.1.81"
port=8888
s.bind((server_ip,port))
while  True :
	x=s.recvfrom(100)
	dn=x[0]
	cliaddr=x[1][0]
	dsz=s.recvfrom(100)[0]
	os.system('lvcreate  --name '+dn+'  --size  '+dsz+'M  cloudvg')
	os.system('mkfs.xfs  /dev/cloudvg/'+dn)
	os.system('mkdir  /mnt/'+dn)
	os.system('mount  /dev/cloudvg/'+dn+'  /mnt/'+dn)
	y="/mnt/"+dn+"   "+cliaddr+"(rw,no_root_squash) \n"
	f=open('/etc/exports','a+')
	f.write(y)
	f.close()
	os.system('exportfs  -r')
