# Websocket Python

> Atividade Referente a Disciplina de Desenvolvimento de Sistemas Distribuídos.

## Atividade

- Meta: implementar, por meio de um estudo de caso, a transmissão de dados com protocolo TCP/UDP

### Regras

- O protocolo de transmissão deve ser UDP
  - Implementações que utilizam UDP como base (ex: HTTP) não são aceitos para essa tarefa
- Avaliação em dupla
- Estudo de caso de livre escolha
  - Exemplos possíveis: transmissão de arquivo (texto, imagem, vídeo), implementação de um jogo simples entre players remotos, sistemas de gerenciamento de contas online, etc.

## Desenvolvimento

> RPCGEN

- Server

```console
❯ cd websocket-python/
❯ python3 server.py localhost
```

- Cliente

```console
❯ cd websocket-python/
❯ python3 client.py
```
