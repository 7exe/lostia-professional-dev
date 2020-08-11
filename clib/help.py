import os
import sys
from command import end


Modules = open("LostiaMain/ModuleConf.config").readlines()
fixedModules = []
for module in Modules:
  fixedModules.append(module.replace("\n",""))
CoreCommands = open("LostiaMain/CoreConf.config").readlines()
fixedCoreCmd = []
for command in CoreCommands:
  fixedCoreCmd.append(command.replace("\n",""))



def MainCommand():
  if(len(sys.argv) > 1):
    if(os.path.exists("LostiaHelp/"+sys.argv[1]+".help")):
      for I in Modules:
        if(I.replace("\n","") == sys.argv[1]):
          Help = open("LostiaHelp/"+sys.argv[1]+".help").readlines()
          for I in Help:
            print(I.replace("\n",""))
            #.replace("#BLUE","\033[38;5;27m").replace("#RESET","\033[39m")
          end(sys.argv)
        else:
          pass
      for I in CoreCommands:
        if(I.replace("\n","") == sys.argv[1]):
          Help = open("LostiaHelp/"+sys.argv[1]+".help").readlines()
          for I in Help:
            print(I.replace("\n",""))
            #.replace("#BLUE","\033[38;5;27m").replace("#RESET","\033[39m").replace("#PINK","\033[38;5;201m").replace("#RED","\033[38;5;1m").replace("#YELLOW","\033[38;5;11m")
          end(sys.argv)
        else:
          pass
      print("No help entry for "+sys.argv[1])
      end(sys.argv)
  
    else:
      print("No help entry for "+sys.argv[1])
      end(sys.argv)
    
  else:
    folder = "LostiaHelp/"
    for file in os.listdir(folder):
      if(".help" in file and file.replace(".help","") in fixedCoreCmd or ".help" in file and file.replace(".help","") in fixedModules):
        filepath = os.path.join(folder, file)
        f = open(filepath, 'r')
        print("%-12s %s" %(file.replace(".help",""),f.read()))
        #.replace("#BLUE","").replace("#RESET","").replace("#PINK","").replace("#RED","").replace("#YELLOW","")
        f.close()
      else:
        pass
    end(sys.argv)

MainCommand()