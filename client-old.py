import zeep

wsdl = 'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'
client = zeep.Client(wsdl=wsdl)

while True:
    print("============= Consulta de CEP =============")
    cep = input("Digite um CEP válido para consulta: ")
    try:
        print(client.service.consultaCEP(cep))
    except Exception as err:
        print("CEP inválido", str(err))
        continue


# import SOAPpy

# # cliente = SOAPProxy('http://localhost:5000/server.php')
# cliente = SOAPpy.SOAPProxy('http://localhost/fileServer.php')

# a = int(input("Digite o valor de a: "))
# b = int(input("Digite o valor de b: "))

# print(cliente.soma(a,b))
# print(cliente.subtracao(a,b))
# print(cliente.multiplicacao(a,b))
# print(cliente.divisao(a,b))
