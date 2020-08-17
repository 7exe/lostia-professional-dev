import command
import sys
import os
import platform

arguments = ["-a","--all","--kernal-name","-n","--nodename","-r","--kernal-release","-v","--kernel-version","-m","--machine","-p","--processor","-o","--operating-system"]

printNewLine = False

if(len(sys.argv) == 1):
  print(platform.system())

count = 0
for I in sys.argv:
  if(count != 0):
    if(I in arguments):
      pass
    else:
      if(I.startswith("-") and I.startswith("--") == False):
        print("uname: invalid option -- '{}'".format(I[-1]))
        print("Try 'help uname' for more information.")
        command.end(sys.argv)
      if(I.startswith("--")):
        print("uname: unrecognized option '{}'".format(I))
        print("Try 'help uname' for more information.")
        command.end(sys.argv)
      if(I.startswith("-") == False and I.startswith("--") == False):
        print("uname: extra operand ‘{}’".format(I))
        print("Try 'help uname' for more information.")
        command.end(sys.argv)
  count+=1

if(command.new_arg_parser("-a") == False and command.new_arg_parser("--all") == False):
  if(command.new_arg_parser("-s") or command.new_arg_parser("--kernal-name")):
    print(platform.system(),end=" ")
    printNewLine = True
  if(command.new_arg_parser("-n") or command.new_arg_parser("--nodename")):
    print(platform.node(),end=" ")
    printNewLine = True
  if(command.new_arg_parser("-r") or command.new_arg_parser("--kernel-release")):
    print(platform.release(),end=" ")
    printNewLine = True
  if(command.new_arg_parser("-v") or command.new_arg_parser("--kernel-version")):
    print(platform.version(),end=" ")
    printNewLine = True
  if(command.new_arg_parser("-m") or command.new_arg_parser("--machine")):
    print(platform.machine(),end=" ")
    printNewLine = True
  if(command.new_arg_parser("-p") or command.new_arg_parser("--processor")):
    print(platform.processor(),end=" ")
    printNewLine = True
  if(command.new_arg_parser("-o") or command.new_arg_parser("--operating-system")):
    print(os.name,end=" ")
    printNewLine = True

else:
  print(platform.system(),end=" ")
  print(platform.node(),end=" ")
  print(platform.release(),end=" ")
  print(platform.version(),end=" ")
  print(platform.machine(),end=" ")
  print(platform.processor(),end=" ")
  print(os.name,end=" ")
  printNewLine = True

if(printNewLine == True):
  print("")