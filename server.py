import rpyc
import sys
import os
from rpyc.utils.server import ThreadedServer


class Service(rpyc.Service):
    def main(args):
        conn = rpyc.classic.connect("localhost")
    
        sys_remoto  = conn.modules.sys  # pega o acesso ao módulo sys remoto.
    
        print(sys_remoto.version)  # imprime a versão do sys remoto
    
        os_remoto = conn.modules.os # pega o acesso ao módulo os remoto
    
        print(os_remoto.uname())  # imprime o uname do os remoto 
        return 0

    def exposed_fileWriter(self, contents, filename, username):
        f = os.listdir("secure")
        if any(filename in f for filename in f):   
            k = open("secure/new"+filename,"wb+")
            if k.mode == "wb+":
                k.write(contents)
                print("\n The file '"+filename+"' from "+username+" has been transmitted to the SERVER successfully! \n")
            k.close()
        else:
            k = open("secure/"+filename,"wb+")
            if k.mode == "wb+":
                k.write(contents)
                print("\n The file '"+filename+"' from "+username+" has been transmitted to the SERVER successfully! \n")
            k.close()
        
    def exposed_download(self, fname):
        for fname in os.listdir("secure"): 
            try:
                f = open("secure/"+fname,"rb")
                if f.mode == "rb":
                    contents = str(f.read())
                f.close()
                return str(contents)
            except IOError:
                return "NF"

    def exposed_disp_list(self):
        return os.listdir("secure")


if __name__ == '__main__':
    if (os.path.isdir("secure/")) == False:
        os.mkdir("secure")
        print("\n Secure Folder Created! \n")

    print("Aguardando...! \n")
    t = ThreadedServer(Service, port = 7000)
    t.start()
