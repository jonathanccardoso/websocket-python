import socket, psutil, os

# host = 'http://127.0.0.1/'
# host = socket.gethostname()
host = socket.gethostbyname("localhost")
print("host", host)

port = 7000
addr = (host, port)

# AF_INET que declara a família do protocolo.
# SOCKET_STREAM, indica que será TCP/IP.
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# qual IP e porta o servidor deve aguardar a conexão.
serv_socket.bind(addr)

# limit connections
serv_socket.listen(10)

print('Aguardando conexao...')
con, client = serv_socket.accept()
print('Conectado!')
print("Aguardando mensagem...")


def shows_ram_memory():
  # psutil: Cross-platform lib for process and system monitoring in Python.
  memory = psutil.virtual_memory()
  print('Memória Total', memory.total / (1024*1024*1024))
  print('Memória Usada', memory.used / (1024*1024*1024))

def files_direct():
  os.system("ls")

def clear():
  os.system("clear")

def top_process():
  os.system("top")


# aguarda um dado enviado pela rede de até 1024 Bytes
conditional = True
while conditional:
  receive = con.recv(1024)
  message_receive = receive.decode('utf8').strip()
  print("Mensagem recebida:", message_receive)
  
  if message_receive == 'exit':
    conditional = False
    # serv_socket.close() # not working in this condiction!
  elif message_receive == '1':
    mem = shows_ram_memory()
    con.send(str(mem).encode()) # send message!
  elif message_receive == '2':
    files_direct()
  elif message_receive == '3':
    clear()
  elif message_receive == '4':
    top_process()
