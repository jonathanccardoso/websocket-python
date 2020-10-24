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

- RPCGEN

Instalações

    > sudo apt update
    > sudo apt install libc-dev-bin
    > sudo apt install make
    > sudo apt install g++
    > make -f Makefile.teste
    > sudo apt install rpcbind

    > nano calculadora.x
    > rpcgen -C calculadora.x

Compilar

    cc servidor.c calculadora_svc.c calculadora_xdr.c -o servidor -lnsl
    cc cliente.c calculadora_clnt.c calculadora_xdr.c -o cliente -lnsl

- Server

```console
❯ cd websocket-python/
❯ ./servidor
```

- Cliente

```console
❯ cd websocket-python/
❯ ./cliente localhost 7 4
```
