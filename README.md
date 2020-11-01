# Distributed systems

> Activity Regarding the Discipline of Distributed Systems Development.

## Activity

- Goal: implement, through a case study, data transmission using the RMI protocol.

## RMI with Pyro4

Pyro is short for Python Remote Objects. It works exactly like the Java RMI (short for Remote Method Invocation) allowing to invoke a method of a remote object (belonging to a different process) exactly as if the object were local (belonging to the same process in which the invocation runs).

The use of an RMI mechanism, in an object-oriented system, involves significant advantages of uniformity and symmetry in the project, as this mechanism enables the modelling of interactions between distributed processes using the same conceptual tool. 

As you can see from the following diagram, Pyro4 enables objects to be distributed in a client/server style; this means that the main parts of a Pyro4 system may switch from a client caller to a remote object, which is called to serve a function:

## Development

```console
❯ cd websocket-python/
❯ python3 -m venv .websocket
❯ source .websocket/bin/activate (linux) ou .websocket\Scripts\activate (windows)
❯ pip3 install Pyro4

❯ python3 -m Pyro4.naming // run service RIM, enable port.
❯ python3 server.py
❯ python3 client.py
```

## Links

- [RMI with Pyro4](https://subscription.packtpub.com/book/programming/9781789533736/6/ch06lvl1sec50/rmi-with-pyro4)
- [RMI Python Medium](https://medium.com/@__biancarosa/writing-distributed-applications-with-python-smart-objects-as-a-java-rmi-alternative-4ba9a812567d)
- [Docs Pyro4](https://pyro4.readthedocs.io/en/stable/intro.html)
