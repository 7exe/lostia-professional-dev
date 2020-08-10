import sys
from command import end
import os


hidden = open("LostiaMain/hidden.config").readlines()
modules = open("LostiaMain/ModuleConf.config").readlines()
coreCmd = open("LostiaMain/CoreConf.config").readlines()


def run_command(command):
  canContinue = False
  for I in modules:
    if(command.split(" ")[0] == I.replace("\n","")):
      canContinue = True

  for I in coreCmd:
    if(command.split(" ")[0] == I.replace("\n","")):
      canContinue = True


  if(canContinue == False):

    print(command.split(" ")[0]+": command not found")
    end(sys.argv)



  if(command.split(" ")[0] in hidden):

    print(command.split(" ")[0]+": command not found")
    end(sys.argv)
  elif(os.path.isfile("clib/"+command.split(" ")[0]+".py")):
    pass
  else:

    print(command.split(" ")[0]+": command not found")
    end(sys.argv)
  
loggedInUser = open("LostiaFiles/user.data").read()
if(loggedInUser == "guest"):
  print("!: Permission Denied")
  end(sys.argv)
historyAsArray = open("LostiaFiles/.gripple_history").readlines()

if(len(sys.argv)>1):
  if("-" not in sys.argv):
      if(int(sys.argv[1])<len(historyAsArray)):
        command = historyAsArray[int(sys.argv[1])-1].replace("\n","")
        print(command)
        run_command(command)
        with open("LostiaFiles/.gripple_history","a") as history:
          history.write(command+"\n")
          history.close()
        os.system("python clib/"+command.split(" ")[0].replace("\n","")+".py"+" "+command.replace(command.split(" ")[0],""))
        end(sys.argv)
      else:
        print("History line not found")
        end(sys.argv)
  else:
    lastRunnedCommand = historyAsArray[len(historyAsArray)-1].replace("\n","")
    print(lastRunnedCommand)
    run_command(lastRunnedCommand)
    with open("LostiaFiles/.gripple_history","a") as history:
          history.write(lastRunnedCommand+"\n")
          history.close()
    os.system("python clib/"+lastRunnedCommand.split(" ")[0].replace("\n","")+".py"+" "+lastRunnedCommand.replace(lastRunnedCommand.split(" ")[0],""))
    end(sys.argv)
else:
  print("!: ! history line / ! -")
  end(sys.argv)