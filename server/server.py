from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client, os

def sayHello():
    return 'Hello World From XMLRPCServer'

def enviaArquivo():
     with open("starwars.jpg", "rb") as handle:
        return xmlrpc.client.Binary(handle.read())

def lerArquivo(file_name):
    f = open(file_name)
    conteudo = f.read()
    return conteudo

server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor ouvindo na porta 8000")
server.register_function(sayHello, "sayHello")
server.register_function(lerArquivo, "lerArquivo")
server.register_function(enviaArquivo, "enviaArquivo")
server.serve_forever()
