from socket import *
import sys

s = socket(AF_INET, SOCK_DGRAM)

try:
  host = sys.argv[1]
except:
  print("Failed on name hostname, one more argument is missing from the statement!")
  sys.exit()

port = 7000
buf  = 1024
addr = (host, port)

try:
  file_name = sys.argv[2]
except:
  print("Failed on filename, one more argument is missing from the statement!")
  sys.exit()

s.sendto(file_name.encode('utf-8'), addr)

f = open(file_name, "rb")
data = f.read(buf)

while (data):
  if(s.sendto(data, addr)):
    print("Sending file...")
    data = f.read(buf)

s.close()
f.close()
