#!/usr/bin/env  python2
import time

x="""
print  " Press 1  to  check current time  :  "
print  " Press  2  to  open firefox  :       "
print  " Press  3  to Add  two numbers  :   "
print  " Press  4  to reboot your system :  "

"""

print  x
ch=input()

if  ch ==  1 :
	t=time.ctime()
	print  "current time is  :  ",t.split()[3]

else  :
	print  "Wrong choice !!!! "
