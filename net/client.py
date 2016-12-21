#!/usr/bin/env python

from socket import *

localhost = '127.0.0.1'
port = 8088

bufferSize = 1024
address = (localhost, port)

if __name__ == '__main__':
    tcpsock = socket(AF_INET, SOCK_STREAM, 0)
    tcpsock.connect(address)

    tcpsock.send(bytes('hello world for python', 'utf-8'))
    data = tcpsock.recv(bufferSize)
    print(data)
    tcpsock.close()
