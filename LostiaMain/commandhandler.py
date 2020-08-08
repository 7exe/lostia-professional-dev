import os
import sys
import time
from time import sleep
import platform


def get_user_from_keychain():
  keychain = open("LostiaFiles/keychain.keychain").readlines()

  loggedInAs = open("LostiaFiles/user.data").read()

  for user in keychain:
    if(user.split("/")[2] == loggedInAs):
      return user
    else:
      pass
  return "/Guest/guest/NoPass/NoPerm/visable/NoDate/Color/"





try:


  while True:


    Modules = open("LostiaMain/ModuleConf.config").readlines()
    CoreCommands = open("LostiaMain/CoreConf.config").readlines()
    loggedInAs = open("LostiaFiles/user.data").read()
    currentDir = open("LostiaFiles/current.directory").readlines()
    display = "~"
    if(currentDir[0] == "LostiaFiles/root/home/"+loggedInAs+"/" or loggedInAs == "guest" or currentDir[0] == "LostiaFiles/root/"):
      display = "~"
    else:
      if(loggedInAs != "systemadmin"):
        display = currentDir[0].replace("LostiaFiles/root/home/"+loggedInAs,"")
      else:
        display = currentDir[0].replace("LostiaFiles/root/","")
    if(loggedInAs != "systemadmin"):
      if(get_user_from_keychain().split("/")[7] == "Color"):
        Command = input("\033[32m"+loggedInAs+"@"+platform.node()+"\033[39m:\033[34m"+display+"\033[39m$ ")
      else:
        Command = input(loggedInAs+"@"+platform.node()+":"+display+"$ ")
    else:
      if(get_user_from_keychain().split("/")[7] == "NoColor"):
        Command = input("root@"+platform.node()+":"+display+"# ")
      else:
        Command = input("\033[32mroot@"+platform.node()+"\033[39m:\033[34m"+display+"\033[39m# ")

    def onCommand():
      if(Command):
        return True
    def fullMessage():
      return Command

    if(Command == "fe"):
      raise Exception('Lostia timeout by command.')
    execute = ""
    for I in CoreCommands:
      if(Command.split(" ")[0] == I.replace("\n","")):
        execute = "python clib/"+I.replace("\n","")+".py "+Command.split(I.replace("\n",""))[1]
      else:
        pass
    
    for O in Modules:
      if(Command.split(" ")[0] == O.replace("\n","")):
        execute = "python clib/"+O.replace("\n","")+".py "+Command.split(O.replace("\n",""))[1]
      else:
        pass
    if(execute == ""):
      if(Command.split(" ")[0] == ""):
        if(Command.replace(" ","") != ""):
          if(Command.split(" ")[0] == ""):
            print(Command.replace(" ","")+": command not found")
          else:
            print(Command.split(" ")[0]+": command not found")
        else:
          pass
      else:
        print(Command.split(" ")[0]+": command not found")
    os.system(execute)
except UnicodeDecodeError:
  pass
