#/usr/bin/python

import socket
import os
import re
import xml.dom.minidom

#Script path + name
#print os.path.realpath(__file__)
#Script working Dir
#print os.getcwd()

#Define lists
functionlist = []
namelist = []
commandlist = []

#Open xml file with variables
doc = xml.dom.minidom.parse("commands.xml");
tags = doc.getElementsByTagName("tag")
for tag in tags:
    #print tag.getAttribute("function")
    functionlist.append(tag.getAttribute("function"))
    #print tag.getAttribute("name")
    namelist.append(tag.getAttribute("name"))
    #print tag.getAttribute("command")
    commandlist.append(tag.getAttribute("command"))

#remove double names from list
functionlist = list(set(functionlist)) 
#print functionlist
#print namelist
#print commandlist


#Set port for running server
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

#Configure socket
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

#run UDP server
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print "received message:", data

    data = re.sub("[^a-z0-9 ]+","", data, flags=re.IGNORECASE)
    datalist = re.split('\s+', data)
    
    for j, function in enumerate(functionlist):
        #print "d is ", repr(function)
        #print "data is ", repr(datalist[0])
        if function == datalist[0]:
            #print "running ", datalist[0], function
            for i, name in enumerate(namelist):
                if name == datalist[1]:
                    if len(datalist) == 3:
                        print "execute ", datalist[0], datalist[1], commandlist[i], datalist[2]
                        cmd = (commandlist[i] + " " + datalist[2])
                        #print str(cmd)
                        os.system(str(cmd))
                        break
                    else:    
                        print "execute ", datalist[0], datalist[1], commandlist[i]
                        os.system(commandlist[i])
                        break
                else:
                    #print "not found"
                    pass
        else:
            #print "not found"
            pass


