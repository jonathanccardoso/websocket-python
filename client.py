import socket

ip = input('Digite o ip de conexao: ')
port = 7000
addr = ((ip, port))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  client_socket.connect(addr)
except Exception as erro:
  print("Error", str(erro))

while True:
  print("==================")
  print("| (1): Memória    |")
  print("| (2): Diretórios |")
  print("| (3): Limpar     |")
  print("| (4): Processos  |")
  print("| (exit): Sair    |")
  print("==================")
  message = input("Digite uma mensagem para enviar ao servidor: ")

  # sends the data to the server
  client_socket.send(message.encode())
  print('Mensagem enviada!')

  # serves to close the connection between the two applications
  # client_socket.close()
