import socket

obj = socket.socket()
obj.connect(("148.70.44.228",22))

ret = str(obj.recv(1024),encoding="utf-8")
print(ret)