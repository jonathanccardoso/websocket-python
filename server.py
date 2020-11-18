import SOAPpy

def soma(a, b):
  return a + b

def subtracao(a, b):
  return a - b

def divisao(a, b):
  return a / b

def multiplicacao(a, b):
  return a * b

server = SOAPpy.SOAPServer(("localhost", 8080))

server.registerFunction(soma)
server.registerFunction(subtracao)
server.registerFunction(divisao)
server.registerFunction(multiplicacao)

print "Run server..."

server.serve_forever()