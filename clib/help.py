import os
import sys
from command import end
from getkey import getkey, keys

Modules = open("LostiaMain/ModuleConf.config").readlines()
fixedModules = []
for module in Modules:
  fixedModules.append(module.replace("\n",""))
CoreCommands = open("LostiaMain/CoreConf.config").readlines()
fixedCoreCmd = []
for command in CoreCommands:
  fixedCoreCmd.append(command.replace("\n",""))

doPrint = False

def MainCommand():
  os.system("clear")
  def do_the_actuall_command():
    global doPrint
    if(len(sys.argv) > 1):
      if(os.path.exists("LostiaHelp/"+sys.argv[1]+".help")):
        for I in Modules:
          if(I.replace("\n","") == sys.argv[1]):
            Help = open("LostiaHelp/"+sys.argv[1]+".help").readlines()
            for I in Help:
              if(len(I.split("#name"))==3):
                print("NAME")
                print("       "+I.split("#name")[1].replace("\l","\n")+"\n")
              if(len(I.split("#synopsis"))==3):
                print("SYNOPSIS")
                print("       "+I.split("#synopsis")[1].replace("\l","\n")+"\n")
              if(len(I.split("#description"))==3):
                print("DESCRIPTION")
                print("       "+I.split("#description")[1].replace("\l","\n")+"\n")
              if(len(I.split("#options"))==3):
                print("OPTIONS")
                print("       "+I.split("#options")[1].replace("\l","\n")+"\n")
              if(len(I.split("#seealso"))==3):
                print("SEE ALSO")
                print("       "+I.split("#seealso")[1].replace("\l","\n")+"\n")
              if(len(I.split("#exitstatus"))==3):
                print("EXIT STATUS")
                print("       "+I.split("#exitstatus")[1].replace("\l","\n")+"\n")
              if(len(I.split("#examples"))==3):
                print("EXAMPLES")
                print("       "+I.split("#examples")[1].replace("\l","\n")+"\n")
              if(len(I.split("#history"))==3):
                print("HISTORY")
                print("       "+I.split("#history")[1].replace("\l","\n")+"\n")
              if(len(I.split("#bugs"))==3):
                print("BUGS")
                print("       "+I.split("#bugs")[1].replace("\l","\n")+"\n")
              if(len(I.split("#standards"))==3):
                print("STANDARDS")
                print("       "+I.split("#standards")[1].replace("\l","\n")+"\n")
              if(len(I.split("#exitvalues"))==3):
                print("EXIT VALUES")
                print("       "+I.split("#exitvalues")[1].replace("\l","\n")+"\n")
              #.replace("#BLUE","\033[38;5;27m").replace("#RESET","\033[39m")
            print("\n\x1b[6;30;47m(END)\n\x1b[0m")
            doPrint = True
          else:
            pass
        for I in CoreCommands:
          if(I.replace("\n","") == sys.argv[1]):
            Help = open("LostiaHelp/"+sys.argv[1]+".help").readlines()
            for I in Help:
              if(len(I.split("#name"))==3):
                print("NAME")
                print("       "+I.split("#name")[1].replace("\l","\n")+"\n")
              if(len(I.split("#synopsis"))==3):
                print("SYNOPSIS")
                print("       "+I.split("#synopsis")[1].replace("\l","\n")+"\n")
              if(len(I.split("#description"))==3):
                print("DESCRIPTION")
                print("       "+I.split("#description")[1].replace("\l","\n")+"\n")
              if(len(I.split("#options"))==3):
                print("OPTIONS")
                print("       "+I.split("#options")[1].replace("\l","\n")+"\n")
              if(len(I.split("#seealso"))==3):
                print("SEE ALSO")
                print("       "+I.split("#seealso")[1].replace("\l","\n")+"\n")
              if(len(I.split("#exitstatus"))==3):
                print("EXIT STATUS")
                print("       "+I.split("#exitstatus")[1].replace("\l","\n")+"\n")
              if(len(I.split("#examples"))==3):
                print("EXAMPLES")
                print("       "+I.split("#examples")[1].replace("\l","\n")+"\n")
              if(len(I.split("#history"))==3):
                print("HISTORY")
                print("       "+I.split("#history")[1].replace("\l","\n")+"\n")
              if(len(I.split("#bugs"))==3):
                print("BUGS")
                print("       "+I.split("#bugs")[1].replace("\l","\n")+"\n")
              if(len(I.split("#standards"))==3):
                print("STANDARDS")
                print("       "+I.split("#standards")[1].replace("\l","\n")+"\n")
              if(len(I.split("#exitvalues"))==3):
                print("EXIT VALUES")
                print("       "+I.split("#exitvalues")[1].replace("\l","\n")+"\n")
              #.replace("#BLUE","\033[38;5;27m").replace("#RESET","\033[39m")
              #.replace("#BLUE","\033[38;5;27m").replace("#RESET","\033[39m").replace("#PINK","\033[38;5;201m").replace("#RED","\033[38;5;1m").replace("#YELLOW","\033[38;5;11m")
            print("\x1b[6;30;47m(END)\x1b[0m")
            doPrint = True
          else:
            pass
        if(doPrint != True):
          print("No help entry for "+sys.argv[1])
        
  
      else:
        print("No help entry for "+sys.argv[1])
    
    else:
      folder = "LostiaHelp/"
      for file in os.listdir(folder):
        if(".help" in file and file.replace(".help","") in fixedCoreCmd or ".help" in file and file.replace(".help","") in fixedModules):
          filepath = os.path.join(folder, file)
          f = open(filepath, 'r')
          try:
            print("%-12s %s" %(file.replace(".help",""),f.read().split("#description")[1]))
          except IndexError:
            pass
          #.replace("#BLUE","").replace("#RESET","").replace("#PINK","").replace("#RED","").replace("#YELLOW","")
          f.close()
        else:
          pass
  do_the_actuall_command()

MainCommand()
if(doPrint != False):
  while True:
    if(getkey() == 'q'):
      os.system("clear")
      end(sys.argv)