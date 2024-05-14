import socket
import time

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('192.168.5.2', 8081))
conn, addr = sk.accept()
sk.listen(2)
while True:
    print(f'Connected to client: {addr}')
    msg = '欢迎访问服务器！' + "\r\n"
    conn.send(msg.encode('utf-8'))
    time.sleep(2)
