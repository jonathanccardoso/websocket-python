#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==== it`s ok ====
# import zeep

# wsdl = 'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'
# client = zeep.Client(wsdl=wsdl)

# while True:
#     print("============= Consulta de CEP =============")
#     cep = input("Digite um CEP válido para consulta: ")
#     try:
#         print(client.service.consultaCEP(cep))
#     except Exception as err:
#         print("CEP inválido", str(err))
#         continue


# cliente = SOAPProxy('http://localhost:5000/server.php')

# a = int(input("Digite um primeiro valor: "))
# b = int(input("Digite o segundo valor: "))

# print(cliente.soma(a,b))
# print(cliente.subtracao(a,b))
# print(cliente.multiplicacao(a,b))
# print(cliente.divisao(a,b))



import SOAPpy

# server = SOAPpy.SOAPProxy("http://localhost:8080/")
server = SOAPpy.SOAPProxy('http://localhost/fileServer.php?wsdl')

a = 0
b = 0
a = int(input("Digite um primeiro valor: "))
b = int(input("Digite o segundo valor: "))

print("====== Operações matemáticas ======")
print "Operacao de soma:", server.soma(a,b)
print "Operacao de subtracao:", server.subtracao(a,b)
print "Operacao de multiplicacao:", server.multiplicacao(a,b)
print "Operacao de divisao:", server.divisao(a,b)
