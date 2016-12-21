#!/usr/bin/env python

from socket import *
from time import ctime

localhost = '0.0.0.0'
port = 8088

buffer_size = 1024
address = (localhost, port)

if __name__ == '__main__':
    tcpsock = socket(AF_INET, SOCK_STREAM, 0)
    tcpsock.bind(address)
    tcpsock.listen(5)

    while True:
        print('Watting for connections ...')
        tcpclientsock, tcpclientaddr = tcpsock.accept()
        print(bytes('A connected from {0}'.format(tcpclientaddr), 'utf-8'))

        while True:
            data = tcpclientsock.recv(buffer_size)
            if not data:
                break
            tcpclientsock.send(bytes('{0} - {1}'.format(ctime(), data), 'utf-8'))
        tcpclientsock.close()
    tcpsock.close()
