from socket import *
import sys
# import select

host = gethostbyname("localhost")
port = 7000
s = socket(AF_INET, SOCK_DGRAM)
s.bind((host, port))

addr = (host, port)
buf = 1024

print("Waiting received File...")

data, addr = s.recvfrom(buf)
print("Received File:", data.strip())
f = open(data.strip(), 'wb')

data, addr = s.recvfrom(buf)
try:
  while(data):
    f.write(data)
    s.settimeout(2)
    data, addr = s.recvfrom(buf)
except timeout:
  f.close()
  s.close()
  print("File Downloaded")
