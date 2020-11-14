# Websocket Python

> Atividade Referente a Disciplina de Desenvolvimento de Sistemas Distribuídos.

## CORBA

Esclarece e simplifica a troca entre sistemas distribuidos heterogênios, Atuando de modo que os objetos possam se comunicar de forma transparente.

### ORB

Bloco intermediário, responsável por aceitar a requisição do usuário para enviar ao objeto.

### IDL

O Corba utiliza a IDL (baseada em c++), que é puramente declarativa, assim possibilitando acesso a qualquer linguagem.

### Persistência

O Corba prover a persistência, definindo o Persistent Object Service (POS), para ser responsável por armazenar o estado dos estados, utilizando quatro elementos:

- Objetos Persistentes (Persistent Object (POs))
- Gerenciador de Objetos Persistentes (Persistent Objects Manager (POM))
- Serviços de Persistência de Dados (Persistent Data Services (PDSs))
- Base de Dados (Datastores)

## Desenvolvimento

```console
❯ cd websocket-python/
❯ python3 -m venv .websocket
❯ source .websocket/bin/activate (linux) ou .websocket\Scripts\activate (windows)

❯ orbd -ORBInitialPort 1050 -ORBDInitialHost localhost
❯ python3 server.p
❯ python3 client.py
  # http://127.0.0.1/
  # escreva uma mensagem...
```
