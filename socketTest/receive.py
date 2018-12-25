from socket import *
import threading
from time import ctime


def recv(sock, BUFSIZ):
    try:
        data = sock.recv(BUFSIZ)
    except OSError:
        return  # find it was close, then close it
    if data.decode() is '[CHAT]BEGIN':
        print(data.decode())
    elif data.decode() is '[CHAT]END':
        sock.close()
    else:
        print('[%s]' % ctime(), ':', data.decode())


if __name__ == '__main__':
    HOST = '144.70.44.228'
    POST = 30000
    ADDR = (HOST, POST)
    tcpCli = socket(AF_INET, SOCK_STREAM)

    tcpCli.connect(ADDR)

    threadrev = threading.Thread(target=recv, args=(tcpCli, 1024))
    threadrev.start()
    while True:
        data = input()
        if not data:
            break
        tcpCli.send(data.encode())
    tcpCli.close()