#!/usr/bin/env        python2

import time

a=input("plz  enter  a number  :  ")

if  a >  10 and a < 20  :
	print  "number is  great than  10 but not greater to 20  "

elif  a > 20  and  a < 30 :

	t=time.ctime()
	print  "Current time  is  "+t.split()[3]


else :
	print   "NO idea  "



