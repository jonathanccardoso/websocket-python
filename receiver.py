from socket import *
import sys, os

host = gethostbyname("localhost")
port = 7000
s = socket(AF_INET, SOCK_DGRAM)
s.bind((host, port))

addr = (host, port)
buf = 1024

print("Waiting received File...")

try:
  os.mkdir("download")
except:
  pass

folder_download = os.getcwd() + "/download"

data, addr = s.recvfrom(buf)
print("Received File:", data.strip())

new_file = folder_download +"/"+ str(data.decode('utf-8'))

# f = open(data.strip(), "wb")
# f = open(folder_download / data.strip(), "wt")
f = open(new_file, "wt")

data, addr = s.recvfrom(buf)
try:
  while(data):
    f.write(data.decode('utf-8'))
    s.settimeout(2)
    data, addr = s.recvfrom(buf)
except timeout:
  f.close()
  s.close()
  print("File Downloaded")
