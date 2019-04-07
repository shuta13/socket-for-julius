#!/usr/bin/python
# -*- coding: utf-8 -*-
# connection.py

import socket
import string

host = 'localhost'   
port = 10500         

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

data =""
while True:

    while ( string.find(data, "\n.") == -1 ):
        data = data + sock.recv(1024)
    
    strTemp = ""
    for line in data.split('\n'):
        index = line.find('WORD="')
        if index != -1:
            line = line[index+6:line.find('"', index+6)]
            strTemp = strTemp + line
    if (strTemp):
        f = open('input.txt', 'w')
        f.write(strTemp)
        f.close
        print( strTemp )
        break
    data = ""
