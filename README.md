# Websocket Python

> Atividade Referente a Disciplina de Desenvolvimento de Sistemas Distribuídos.

## SOAP

SOAP é um protocolo para troca de informações estruturadas em uma plataforma descentralizada e distribuída. Ele se baseia na Linguagem de Marcação Extensível (XML) para seu formato de mensagem, e normalmente baseia-se em outros protocolos da camada de aplicação.

![SOAP](https://upload.wikimedia.org/wikipedia/commons/5/59/SOAP.svg)

SOAP pode formar a camada base de uma pilha de protocolos de serviços Web, fornecendo um arcabouço básico de mensagens sob o qual se podem construir os serviços Web.

Geralmente servidores SOAP são implementados utilizando-se servidores HTTP, embora isto não seja uma restrição para funcionamento do protocolo. As mensagens SOAP são documentos XML que aderem a uma especificação W3C.

O primeiro esforço do desenvolvimento do SOAP foi implementar RPCs sobre XML.

### Definição

Envelope das mensagens, regras de codificação, convenção RPC, ligação com protocolos subjacentes.

O SOAP é:

- mecanismo para definir a unidade de comunicação,
- mecanismo para lidar com erros,
- mecanismo de extensão que permite evolução,
- mecanismo entre as mensagens SOAP e o HTTP, que permite representar tipos de dados em XML.

## Desenvolvimento

```console
❯ cd websocket-python/
❯ python3 -m venv .websocket
❯ source .websocket/bin/activate (linux) ou .websocket\Scripts\activate (windows)

❯ python client.py
❯ python server.php // or runing php http://localhost/fileServer.php
  # http://127.0.0.1/
  # sending messages...
```

## Links

- [SOAP wiki](https://pt.wikipedia.org/wiki/SOAP)
- [PIP SOAP](https://pypi.org/project/SOAPpy/#using-github)
- [API Github](https://api.github.com/)