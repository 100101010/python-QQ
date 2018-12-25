# import requests
 
# def getWeather(city):
#     r = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=" + city)
#     data = r.json()['data']['forecast'][0]
#     print(r.json())
#     return '{0}: {1}, {2}'.format(city, data['low'], data['high'])
 
# print(getWeather('重庆'))
# import os

# file = os.read(r'F:\web')
# print(file)
# "python.pythonPath": "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python35\\python",
#     "editor.fontSize": 32,
import socket
import sys
from threading import Thread
 
 
class ChatClient:
 
    def __init__(self):
        self.s = socket.socket()
        server = '144.70.44.228'
        port = 1234
        self.s.connect((server, port))   # 连接服务器
        self.run()
 
    def run(self):
        prepareRecv = self.PrepareRecv(self.s)
        prepareRecv.start()
        while True:
            data = input("")
            try:
                self.s.send(data.encode())
                if data == "quit":
                    break
            except:
                print("与服务器连接中断！")
                break
 
        self.s.close()                   # 关闭连接
 
    class PrepareRecv(Thread):
 
        def __init__(self, _socket):
            Thread.__init__(self)
            self.setDaemon = True        # 主线程结束终止子线程
            self._socket = _socket
 
        def run(self):
            while True:
                try:
                    readText = self._socket.recv(1024).decode()
                    if readText == "":
                        self._socket.close()
                        break
                    else:
                        print(readText)
                except:
                    self._socket.close()
                    break
 
 
if __name__ == '__main__':
    ChatClient()