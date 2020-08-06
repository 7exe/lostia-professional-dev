import os
import sys
from command import end


Modules = open("LostiaMain/ModuleConf.config").readlines()
CoreCommands = open("LostiaMain/CoreConf.config").readlines()



def MainCommand():
  if(len(sys.argv) > 1):
    if(os.path.exists("LostiaHelp/"+sys.argv[1]+".help")):
      for I in Modules:
        if(I.replace("\n","") == sys.argv[1]):
          Help = open("LostiaHelp/"+sys.argv[1]+".help").readlines()
          for I in Help:
            print(I.replace("\n",""))
          end(sys.argv)
        else:
          pass
      for I in CoreCommands:
        if(I.replace("\n","") == sys.argv[1]):
          Help = open("LostiaHelp/"+sys.argv[1]+".help").readlines()
          for I in Help:
            print(I.replace("\n",""))
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
      if(".help" in file):
        filepath = os.path.join(folder, file)
        f = open(filepath, 'r')
        print(file.replace(".help","") +" - "+f.read())
        f.close()
      else:
        pass
    end(sys.argv)

MainCommand()