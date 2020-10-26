import xmlrpc.client
import os
import sys

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
print("Bem Vindo ao Gerenciador de Arquivos!")

print("===========MENU==========")
print("| (1): Enviar um Arquivo|")
print("| (2): Ler um Arquivo   |")
print("=========================")
menu = input("Escolha uma opção no Menu: ")

if menu == "1":
    print("VOCÊ ESCOLHEU ENVIAR UM ARQUIVO")
    print("")
    arquivo = input("Digite o nome do arquivo: ")
    folder_download = os.getcwd() + "/download"
    new_file = folder_download +"/"+ arquivo
    with open(new_file, "wb") as handle:
        handle.write(proxy.enviaArquivo(arquivo).data)

    print("Mensagem do Servidor: %s" %handle)
elif menu == "2":
    print("VOCÊ ESCOLHEU LER UM ARQUIVO")
    print("")
    arquivo = input("Digite o nome do arquivo: ")
    livro = proxy.lerArquivo(arquivo)
    print("Mensagem do Servidor: %s" %livro)
else:
    print("Valor inválido")

# hello = proxy.sayHello()
#
# arquivo = input("Digite o nome do arquivo: ")
# folder_download = os.getcwd() + "/download"
# new_file = folder_download +"/"+ arquivo
# with open(new_file, "wb") as handle:
#     handle.write(proxy.enviaArquivo().data)
#
# print("Mensagem do Servidor: %s" %handle)
