import rpyc
import os
import shutil
import sys
from os import path
from zipfile import ZipFile
from shutil import make_archive

c = rpyc.connect("localhost", 7000)

try:
    filename = sys.argv[1]
except:
    c.close()
    
# print(c.root.disp_list()) # name file
if(filename != ""):
    content = c.root.download(filename)

    if content != "NF":
        k = open(filename, "rb+")
        if k.mode == "rb+":
            k.write(content.encode('utf-8'))
        print("'" + filename + "' has been transfered successfully!")
        k.close()
    else:
        print("File does not exist")

c.close()


#   user_input = input("Hello "+str(username)+" \n Enter 'show' to see or download file \n Enter 'share' to share your files  \n  press exit() to leave\n")
#   # Open the User entered file and read contents from it in binary mode 
#   if user_input != "exit()":  # Give user the  
#       if user_input!="show":
#         filename= input("Enter filename to share")
#         try:
#           if(path.isfile(filename)):    #For file input,send
#               f = open(filename,"rb")
#               if f.mode == "rb":
#                   contents = str(f.read())
#               f.close()
#           if(path.isdir(filename)):     #For directory input,zip and send
#               shutil.make_archive("newarchive", "zip", filename)
#               f = open("newarchive.zip","rb")
#               filename=filename+".zip"
#               if f.mode == "rb":
#                   contents = str(f.read())
#               f.close()
#               os.remove("newarchive.zip")
#           c.root.fileWriter(contents,filename,username)
#           print("\n The file: "+str(filename)+" has been shared \n")
#         except IOError:
#           print("\n Couldn't send the file  \n")
#       else:
#         # print(c.root.disp_list())
#         filename= input("Enter filename to download or press c to continue: ")
#         if(filename!="c"):
#           content=c.root.download(filename)
#           if content!="NF":
#             k = open(filename,"wb+")
#             if k.mode == "wb+":
#               k.write(content)
#             print("'"+filename+"' has been transfered successfully!")
#             k.close()
#           else:
#             print("File does not exist")
#   else:
#     break

# c.close()
