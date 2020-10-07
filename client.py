import socket

ip = input('Digite o ip de conexao: ')
port = 7000
addr = ((ip, port))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
mensagem = input("Digite uma mensagem para enviar ao servidor: ")

# que faz o envio do dado para servidor
client_socket.send(mensagem.encode())
print('Mensagem enviada!')

# serve para fechar a conexão entre os dois aplicativos
client_socket.close()
