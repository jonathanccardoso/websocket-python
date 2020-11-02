from datetime import datetime

import Pyro4
import re
import os


server = Pyro4.Proxy(f"PYRONAME:chat.server") # use name server object lookup uri shortcut

def start_chatting():
  text = ''
  while (text != 'exit'):
    print("Envie mensagens... \nSe quiser fazer download de algum arquivo escreva Download")
    text = input("❯ ") 
    now = datetime.now()

    server.send_message(text)

    if 'download' in text.lower():
      file_name = input("Digite o nome do arquivo: ")
      
      folder_download = os.getcwd() + "/download"
      new_file = folder_download +"/"+ file_name

      # output_file = open(file_name, "wb")
      # output_file.write(server.download(file_name))
      # output_file.write(server.download(file_name).encode("ascii", "replace", "utf-8"))
      # output_file.write(server.download(file_name)).encode("ascii", "replace", "utf-8")
      # output_file.write(b'sdasdad').encode("ascii", "replace", "utf-8")
      # output_file.write(b'sdasdad')      
      # output_file.close()

      with open(new_file, "wb") as handle:
        handle.write(server.download(file_name).encode("utf-8"))
        # handle.write(server.download(file_name))
        # handle.write(b"sdda")

      print("Downloaded file: {}".format(file_name))
    
    print(f'Sent \n')


if __name__ == '__main__':
  try:
    start_chatting()
  except (KeyboardInterrupt, EOFError):
    print('Bye!')
exit
