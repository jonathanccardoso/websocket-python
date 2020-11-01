from datetime import datetime

import Pyro4


server = Pyro4.Proxy(f"PYRONAME:chat.server") # use name server object lookup uri shortcut

def start_chatting():
  text = ''
  while (text != 'exit'):
    text = input("... ")
    now = datetime.now()
    server.send_message(text)
    
    print(f'Sent at \n')
    # print(f'sent at {now:%H:%M:%S} \n')


if __name__ == '__main__':
  try:
    start_chatting()
  except (KeyboardInterrupt, EOFError):
    print('Bye!')
exit
