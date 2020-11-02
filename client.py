from datetime import datetime

import Pyro4
import re
import os


server = Pyro4.Proxy(f"PYRONAME:chat.server") # use name server object lookup uri shortcut

def start_chatting():
  text = ''
  while (text != 'exit'):
    print("Envie mensagens... \nSe quiser fazer download de algum arquivo escreva Download")

    # text = input("... ")
    text = input("❯ ") 
    now = datetime.now()

    server.send_message(text)

    if 'download' in text.lower():
      file_name = input("Digite o nome do arquivo: ")
      
      folder_download = os.getcwd() + "/download"
      new_file = folder_download +"/"+ file_name
      print("new_file", new_file)

      # output_file = open(new_file, "wb")
      # output_file.write(server.download(file_name))

      with open(new_file, "wb") as handle:
        # handle.write(server.download(file_name).data)
        handle.write(server.download(file_name))

      output_file.close()
      print("Downloaded file: {}".format(file_name))
    
    print(f'Sent at \n')


if __name__ == '__main__':
  try:
    start_chatting()
  except (KeyboardInterrupt, EOFError):
    print('Bye!')
exit
