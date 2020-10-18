# Websocket Python

> Atividade Referente a Disciplina de Desenvolvimento de Sistemas Distribuídos.

## Atividade

- Meta: implementar, por meio de um estudo de caso, a transmissão de dados com protocolo TCP/UDP

### Regras

- O protocolo de transmissão deve ser TCP/UDP
  - Implementações que utilizam TCP/UDP como base (ex: HTTP) não são aceitos para essa tarefa
- Avaliação em dupla
- Estudo de caso de livre escolha
  - Exemplos possíveis: transmissão de arquivo (texto,imagem, vídeo), implementação de um jogo simples entre players remotos, sistemas de gerenciamento de contas online, etc.

## Desenvolvimento

- TCP

```console
❯ cd websocket-python/
❯ python3 -m venv .websocket
❯ source .websocket/bin/activate (linux) ou .websocket\Scripts\activate (windows)
❯ python3 server.py
❯ python3 client.py
  # http://127.0.0.1/
  # escreva uma mensagem...
```

- UDP

```console
❯ python3 recevier.py
❯ python3 sender.py localhost filename.txt
```

## Links

- [socket python](https://www.alura.com.br/artigos/entendendo-socket-no-python-criando-um-bot-de-irc)
