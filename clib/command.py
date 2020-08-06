import os
import sys
from getpass import getpass

loggedInAs = open("LostiaFiles/user.data").read()
isLoggedIn = False

def end(argv):
  if("-k" in argv):
    exit()
  else:
    exit()
  

Hidden = open("LostiaMain/hidden.config").readlines()

users = open("LostiaFiles/keychain.keychain")

currentUser = open("LostiaFiles/user.data").read()

def ask_for_password(commandname,passwordownername,maxattempts,password):
  count = 1
  while count<maxattempts+1:
    askForPassword = getpass("["+commandname+"] enter password for "+passwordownername+": ")
    if(askForPassword == password):
          count = 4
          return True
    else:
      if(count != maxattempts):
        print("Sorry, try again.")
      count+=1
  print(commandname+": 3 incorrect password attempts.")
  end(sys.argv)
  

def check_for_permission():
  if(currentUser == "guest"):
    split = sys.argv[0].split("/")
    lenSplit = len(split)
    print(split[lenSplit-1].replace(".py","")+": PERMISSION DENIED.")
    end(sys.argv)
  else:
    for user in users:
      if(user.split("/")[2] == currentUser):
        if(user.split("/")[4] == "sysadmin" or user.split("/")[4] == "admin"):
          return True
        else:
          print("Invalid Permission")
          end(sys.argv)
      else:
        pass
    





def force_run_command(command):
  check_for_permission()
  if(command in Hidden):
    raise Exception("Attempted to run '"+command+"', which does not exist or it's hidden.")
    end(sys.argv)
  elif(os.path.isfile("clib/"+command.split(" ")[0]+".py")):
    
    print(sys.argv[0]+" is trying to use force_run_command with the command '"+command+"', which can be harmful to your device, do you want to run it? y/n")
    Input = input("> ")
    if(Input == "y"):



      if(len(command.split(" "))==1):
        print("Ran "+command)
      elif(len(command.split(" "))>1):
        print("Ran "+command.split(" ")[0]+" with the arguments "+command.replace(command.split(" ")[0]+" ",""))
      os.system("python clib/"+command.split(" ")[0]+".py"+" "+command.replace(command.split(" ")[0],""))
    elif(Input == "n"):
      end(sys.argv) 
  else:
    raise Exception("Attempted to run '"+command+"', which does not exist or it's hidden.")
    end(sys.argv)
  