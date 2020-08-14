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
  def do_the_actuall_command():
    global doPrint
    if(len(sys.argv) > 1):
      if(os.path.exists("LostiaHelp/"+sys.argv[1]+".help")):
        curlString = ""
        for I in Modules:
          if(I.replace("\n","") == sys.argv[1]):
            Help = open("LostiaHelp/"+sys.argv[1]+".help").readlines()
  
            for I in Help:
              if(len(I.split("<name>"))==3):
                curlString+="NAME\n"
                curlString+="       "+I.split("<name>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<synopsis>"))==3):
                curlString+="SYNOPSIS\n"
                curlString+="       "+I.split("<synopsis>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<description>"))==3):
                curlString+="DESCRIPTION\n"
                curlString+="       "+I.split("<description>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<options>"))==3):
                curlString+="OPTIONS\n"
                curlString+="       "+I.split("<options>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<seealso>"))==3):
                curlString+="SEE ALSO\n"
                curlString+="       "+I.split("<seealso>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<exitstatus>"))==3):
                curlString+="EXIT STATUS\n"
                curlString+="       "+I.split("<exitstatu>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<examples>"))==3):
                curlString+="EXAMPLES\n"
                curlString+="       "+I.split("<examples>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<history>"))==3):
                curlString+="HISTORY\n"
                curlString+="       "+I.split("<history>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<bugs>"))==3):
                curlString+="BUGS\n"
                curlString+="       "+I.split("<bugs>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<standards>"))==3):
                curlString+="STANDARDS\n"
                curlString+="       "+I.split("<standards>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<exitvalues>"))==3):
                curlString+="EXIT VALUES\n"
                curlString+="       "+I.split("<exitvalues>")[1].replace("\l","\n")+"\n"
              #.replace("#BLUE","\033[38;5;27m").replace("#RESET","\033[39m")
            curlString+="\n\x1b[6;30;47m(END)\n\x1b[0m"
            doPrint = True
          else:
            pass
        for I in CoreCommands:
          if(I.replace("\n","") == sys.argv[1]):
            Help = open("LostiaHelp/"+sys.argv[1]+".help").readlines()
            for I in Help:
              if(len(I.split("<name>"))==3):
                curlString+="NAME\n"
                curlString+="       "+I.split("<name>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<synopsis>"))==3):
                curlString+="SYNOPSIS\n"
                curlString+="       "+I.split("<synopsis>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<description>"))==3):
                curlString+="DESCRIPTION\n"
                curlString+="       "+I.split("<description>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<options>"))==3):
                curlString+="OPTIONS\n"
                curlString+="       "+I.split("<options>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<seealso>"))==3):
                curlString+="SEE ALSO\n"
                curlString+="       "+I.split("<seealso>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<exitstatus>"))==3):
                curlString+="EXIT STATUS\n"
                curlString+="       "+I.split("<exitstatu>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<examples>"))==3):
                curlString+="EXAMPLES\n"
                curlString+="       "+I.split("<examples>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<history>"))==3):
                curlString+="HISTORY\n"
                curlString+="       "+I.split("<history>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<bugs>"))==3):
                curlString+="BUGS\n"
                curlString+="       "+I.split("<bugs>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<standards>"))==3):
                curlString+="STANDARDS\n"
                curlString+="       "+I.split("<standards>")[1].replace("\l","\n")+"\n"
              if(len(I.split("<exitvalues>"))==3):
                curlString+="EXIT VALUES\n"
                curlString+="       "+I.split("<exitvalues>")[1].replace("\l","\n")+"\n"
              #.replace("#BLUE","\033[38;5;27m").replace("#RESET","\033[39m")
              #.replace("#BLUE","\033[38;5;27m").replace("#RESET","\033[39m").replace("#PINK","\033[38;5;201m").replace("#RED","\033[38;5;1m").replace("#YELLOW","\033[38;5;11m")
            curlString+="\x1b[6;30;47m(END)\x1b[0m"
            doPrint = True
          else:
            pass
        if(doPrint != True):
          print("No help entry for "+sys.argv[1])
        else:
          os.system("clear")
          print(curlString)
        
  
      else:
        print("No help entry for "+sys.argv[1])
      
    
    else:
      folder = "LostiaHelp/"
      for file in os.listdir(folder):
        if(".help" in file and file.replace(".help","") in fixedCoreCmd or ".help" in file and file.replace(".help","") in fixedModules):
          filepath = os.path.join(folder, file)
          f = open(filepath, 'r')
          try:
            print("%-12s %s" %(file.replace(".help",""),f.read().split("<description>")[1]))
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