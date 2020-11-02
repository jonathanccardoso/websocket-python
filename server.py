from datetime import datetime

import Pyro4
import os


# Decorator on the class definition to tell Pyro it is allowed to access the class remotely.
@Pyro4.expose
class Chat(object):
  def send_message(self, text):
    now = datetime.now()
    print(f'{text} - Received at {now:%H:%M:%S} \n')

  def download(self, file_name):
    print("Conteúdo do arquivo")
    print("file_name", file_name)

    folder_download = os.getcwd() + "/download"
    new_file = folder_download +"/"+ file_name

    f = open(file_name, 'rb')
    
    context = str(f.read())
    
    return str(context)


def start_server():
  daemon = Pyro4.Daemon() # This is the part that listens for remote method calls, dispatches to actual objects
  ns = Pyro4.locateNS() # Get a proxy for a name server somewhere in the network. If you’re not providing host or port arguments, the configured defaults are used.
  uri = daemon.register(Chat) # register the Chat as a Pyro object
  ns.register('chat.server', str(uri)) # register the object with a name in the name server

  print(f'Ready to listen...')
  daemon.requestLoop()


if __name__ == '__main__':
  try:
    start_server()
  except (KeyboardInterrupt, EOFError):
    print('Bye!')
exit
