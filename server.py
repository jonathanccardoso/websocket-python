import socket

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

# limite de conexões
serv_socket.listen(10)

print('Aguardando conexao...')
con, cliente = serv_socket.accept()
print('Conectado!')
print("Aguardando mensagem...")

# aguarda um dado enviado pela rede de até 1024 Bytes
recebe = con.recv(1024)
print("Mensagem recebida: ", recebe.decode('utf8').strip())
serv_socket.close()
