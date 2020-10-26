import xmlrpc.client
import os
import sys

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
print("Bem Vindo ao Gerenciador de Arquivos!")

# livro = proxy.lerArquivo(arquivo)

hello = proxy.sayHello()

arquivo = input("Digite o nome do arquivo: ")
folder_download = os.getcwd() + "/download"
new_file = folder_download +"/"+ arquivo
with open(new_file, "wb") as handle:
    handle.write(proxy.enviaArquivo().data)

print("Mensagem do Servidor: %s" %handle)
