#!/usr/bin/env python2

import  os,commands,time,socket

print  "Welcome to My Project !!"
time.sleep(1)
print  "Plz Wait  for Services  !!"


x="""
Press  1  To   Access   SAAS  :
Press  2  To   Access   StAAS  :
Press  3  To   Access   IAAS  :
Press  4  To   Access   PAAS  :
"""
print  x
ch=raw_input()

if  ch  ==  '1'  :
	execfile('saas.py')
elif  ch  ==  '2' :
	execfile('staas.py')
