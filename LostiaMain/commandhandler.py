import os
import sys
import time
from time import sleep
import platform
from difflib import SequenceMatcher

def set_terminal_title(title):
  print('\33]0;'+title+'\a', end='')
  sys.stdout.flush()

def get_user_from_keychain():
  keychain = open("LostiaFiles/keychain.keychain").readlines()

  loggedInAs = open("LostiaFiles/user.data").read()

  for user in keychain:
    if(user.split("/")[2] == loggedInAs):
      return user
    else:
      pass
  return "/Guest/guest/NoPass/NoPerm/visable/NoDate/Color/"







while True:
  try:


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
        set_terminal_title(loggedInAs+"@"+platform.node()+":"+display+"$")
      else:
        Command = input(loggedInAs+"@"+platform.node()+":"+display+"$ ")
        set_terminal_title(loggedInAs+"@"+platform.node()+":"+display+"$ ")
    else:
      if(get_user_from_keychain().split("/")[7] == "NoColor"):
        Command = input("root@"+platform.node()+":"+display+"# ")
        set_terminal_title("root@"+platform.node()+":"+display+"# ")
      else:
        Command = input("\033[32mroot@"+platform.node()+"\033[39m:\033[34m"+display+"\033[39m# ")
        set_terminal_title("root@"+platform.node()+":"+display+"# ")

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
      if(Command.split(" ")[0] == O.replace("\n","") and Command.startswith("!") == False):
        execute = "python clib/"+O.replace("\n","")+".py "+Command.split(O.replace("\n",""))[1]
      else:
        pass
    if(execute == ""):
      dontPrint = False
      finalResults = []
      if(Command != "" and Command.replace(" ","") != "" and Command.startswith(" ") != True):
        for I in CoreCommands:
          if(SequenceMatcher(a=I,b=Command.split(" ")[0]).ratio()>=0.6):
            finalResults.append("  command '"+I.replace("\n","")+"' from core commands")
            dontPrint = True
          else:
            pass
        for I in Modules:
          if(SequenceMatcher(a=I,b=Command.split(" ")[0]).ratio()>=0.6):
            # or I.startswith(Command.split(" ")[0])
            finalResults.append("  command '"+I.replace("\n","")+"' from module commands")
            dontPrint = True
          else:
            pass
        if(dontPrint == True):
          print("ash: "+"Command '"+Command.split(" ")[0]+"' not found, did you mean:\n")
          for command in finalResults:
            print(command)
          print()
        #print("Try: sudo apt install <deb name>")
      if(dontPrint == False):
        if(Command.split(" ")[0] == ""):
          if(Command.replace(" ","") != ""):
            if(Command.split(" ")[0] == ""):
              print("ash: command not found: "+Command.lstrip().split(" ")[1])
            else:
              print("ash: command not found: "+Command.split(" ")[0])
          else:
            pass
        else:
          print("ash: command not found: "+Command.split(" ")[0])
    if(Command.replace(" ","") != "" and Command.startswith("!") == False):
      with open("LostiaFiles/.gripple_history","a") as history:
          history.write(Command+"\n")
          history.close()
    os.system(execute)
    dontPrint = False
  except UnicodeDecodeError:
    continue
