import os
import sys
from command import end
import platform



def setTerminalColor():
  if(platform.system() == "Linux"):
    os.system("setterm -background blue -foreground white")
    print("")
    os.system("clear")
    os.system("setterm -background blue -foreground white")
  else:
    pass


CoreCommands = open("LostiaMain/CoreConf.config").readlines()
Hidden = open("LostiaMain/hidden.config").readlines()
CoreCommandsFixed = []
ModuleConfigFixed = []
HiddenFixed = []
Modules = []


def PrintModules():
  print("======== Module Manager ========")
  for I in FixedInFileCommands:
      if(I.replace(".py","") in CoreCommandsFixed or I.replace(".py","") in HiddenFixed):
        pass
      else:
        Modules.append(I.replace(".py",""))
        box = ""
        for d in range(len(I.replace(".py",""))):
          box = box + "═"
        if(I.replace(".py","") in ModuleConfigFixed):
          print("╔"+box+"╗")
          print("║"+I.replace(".py","")+"║  [ENABLED]")
          print("╚"+box+"╝")
        else:
          print("╔"+box+"╗")
          print("║"+I.replace(".py","")+"║")
          print("╚"+box+"╝")

setTerminalColor()

for I in Hidden:
  HiddenFixed.append(I.replace("\n",""))


for I in CoreCommands:
  CoreCommandsFixed.append(I.replace("\n",""))

def UpdateModuleConfFixed():
  ModuleConfigFixed.clear()
  moduleConfig = open("LostiaMain/ModuleConf.config").readlines()
  for I in moduleConfig:
    ModuleConfigFixed.append(I.replace("\n",""))

printmodules = 1
UpdateModuleConfFixed()

def enablecommand():
  if(Command.split(" ")[0] == "enable"):
    try:
      UpdateModuleConfFixed()
      if(len(Command.split(" "))<2):
        return print("enable: must specify target")
      for I in Modules:
        if(Command.split(" ")[1] == I):
          UpdateModuleConfFixed()
          if(Command.split(" ")[1].replace(".py","") in ModuleConfigFixed):
            print("This module is already enabled!")
            return None
            break
          else:
           with open("LostiaMain/ModuleConf.config", "a") as f:
              f.write(I.replace(".py","")+"\n")
              f.close()
           UpdateModuleConfFixed()
           setTerminalColor()
           PrintModules()
           break
          
    except:
      print("Failed to enable module.")

def disablecommand():
  if(Command.split(" ")[0] == "disable"):
      UpdateModuleConfFixed()
      if(len(Command.split(" "))<2):
        return print("disable: must specify target")
      for I in Modules:
        if(Command.split(" ")[1] == I):
          if(Command.split(" ")[1].replace(".py","") in ModuleConfigFixed):
            pass
          else:
            print("This module is already disabled!")
            return None
            break
          for B in ModuleConfigFixed:
            if(B == Command.split(" ")[1].replace(".py","")):
              ModuleConfigFixed.remove(B)
              break
          with open("LostiaMain/ModuleConf.config", "w") as a:
            for A in ModuleConfigFixed:
              a.write(A+"\n")
            a.close()
          UpdateModuleConfFixed()
          setTerminalColor()
          PrintModules()
          break



#open(".LostiaMain/ModuleConf.config", 'w').close()


InFileCommands = os.listdir("clib/")

FixedInFileCommands = []

for I in InFileCommands:
  if(".py" in I):
    FixedInFileCommands.append(I)
  else:
    pass

while True:
  if(printmodules == 1):
    PrintModules()
    printmodules = 0

  #Command Handling

  Command = input(">> ")

  if(Command == "exit"):
    os.system("clear")
    end(sys.argv)

  enablecommand()
  disablecommand()
  

