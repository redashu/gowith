#!/usr/bin/python2

import  cgi
import  commands

print  "content-type:text/html"
print  ""

x=cgi.FieldStorage()
d_name=x.getvalue('d')
d_size=x.getvalue('s')

print  "<pre>"
print  commands.getoutput('sudo  lvcreate  --name '+d_name+'  --size '+d_size+'M  cloudvg')
print  commands.getoutput('sudo mkfs.xfs   /dev/cloudvg/'+d_name)
print commands.getoutput('sudo mkdir  /mnt/'+d_name)
print  commands.getoutput('sudo mount  /dev/cloudvg/'+d_name+'  /mnt/'+d_name)

print  "</pre>"

