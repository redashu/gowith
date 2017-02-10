#!/usr/bin/env  python2
import time
import  webbrowser
import  commands

x="""
print  " Press 1  to  check current time  :  "
print  " Press  2  to  open web browser  :       "
print  " Press  3  to Add  two numbers  :   "
print  " Press  4  to reboot your system :  "

"""

print  x
ch=input()

if  ch ==  1 :
	t=time.ctime()
	print  "current time is  :  ",t.split()[3]

elif  ch  ==  2 :
	webbrowser.open_new_tab('http://www.google.com')

elif  ch  ==  3 :
	n1=input("enter  number 1 :  ")
	n2=input("enter  number 2 :  ")
	print  "sum of two given numbers  is  ",n1+n2
elif  ch == 4 :
	commands.getouput('reboot')
else  :
	print  "Wrong choice !!!! "
