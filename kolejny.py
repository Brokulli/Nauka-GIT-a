#! /usr/bin/python

import os

f=os.popen("id")    #pobiera id
x=f.read()  #przechowuje id
print(x)    #drukuje id

f=os.popen("cat /proc/cpuinfo | grep cores") #grep cores - pokazywanie tylko ilosci procesorow
y=f.read()
y=y.split('\n')
w=len(y)-1
print(w)

f=os.popen("cat /proc/meminfo | grep MemFree") #grep MemFree - tylko wolnej pamieci
z=f.read()
print(z)
