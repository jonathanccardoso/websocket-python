#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SOAPpy

# server = SOAPpy.SOAPProxy("http://localhost:8080/")
server = SOAPpy.SOAPProxy('http://localhost/fileServer.php')

a = 0
b = 0
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

print("====== Operações matemáticas ======")
print "Operacao de soma:", server.soma(a,b)
print "Operacao de subtracao:", server.subtracao(a,b)
print "Operacao de multiplicacao:", server.multiplicacao(a,b)
print "Operacao de divisao:", server.divisao(a,b)
