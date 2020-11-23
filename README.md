# Websocket Python

> Atividade Referente a Disciplina de Desenvolvimento de Sistemas Distribuídos.

## API REST

API REST, também chamada de API RESTful, é uma interface de programação de aplicações que segue conformidade com as restrições da arquitetura REST. A sigla REST significa Representational State Transfer (Transferência Representacional de Estado, em português).

Uma interface de programação de aplicações (API) é um conjunto de definições e protocolos para criar e integrar softwares de aplicações. Às vezes, as APIs são referidas como um contrato entre um provedor e um usuário de informações, estabelecendo o conteúdo exigido pelo consumidor (a chamada) e o conteúdo exigido pelo produtor (a resposta). Por exemplo, uma API de um serviço meteorológico pode especificar que o usuário forneça um CEP e o produtor responda em duas partes, a primeira contendo a temperatura mais elevada e a segunda com a temperatura mais baixa.

- REST não é um protocolo ou padrão, mas sim um conjunto de princípios de arquitetura. Os desenvolvedores de API podem implementar a arquitetura REST de maneiras variadas.

### API GATEWAY

O Amazon API Gateway é um serviço da AWS para criação, publicação, manutenção, monitoramento e proteção de APIs REST e WebSocket em qualquer escala. Os desenvolvedores de APIs podem criar APIs que acessem serviços da AWS ou outros serviços da Web, bem como dados armazenados na Nuvem AWS.

Como um desenvolvedor de APIs do API Gateway, é possível criar APIs para uso em suas próprias aplicações cliente. Ou você pode disponibilizar suas APIs para desenvolvedores de aplicativos de terceiros. Para obter mais informações, consulte Quem usa o API Gateway?.

O API Gateway cria APIs RESTful que:

- São baseadas em HTTP.
- Habilitam a comunicação cliente-servidor sem estado.
- Implementam os métodos HTTP padrão, como GET, POST, PUT, PATCH e DELETE.

## Desenvolvimento

```console
❯ cd websocket-python/
❯ python3 -m venv .websocket
❯ source .websocket/bin/activate (linux) ou .websocket\Scripts\activate (windows)
❯ python3 manage.py runserver
❯ pip freeze > requirements.txt

// open file index.html to application front.
```

### Endpoints

- http://localhost:8000/api/users/
- http://localhost:8000/api/user/github/{username}
- http://localhost:8000/api/user/zipcode/{zipcode}

## Links

- [SOAP wiki](https://pt.wikipedia.org/wiki/SOAP)
- [PIP SOAP](https://pypi.org/project/SOAPpy/#using-github)
- [API Github](https://api.github.com/)
