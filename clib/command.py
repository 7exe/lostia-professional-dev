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

def new_arg_parser(argument):
  import sys
  if(argument == "" or argument.replace(" ","") == ""):
    raise ValueError("argument value cannot be nothing")
  else:
    if(argument in sys.argv):
      return True
    else:
      return False





def who_am_i():
  if(currentUser != "systemadmin"):
    return currentUser
  else:
    return "root"
    
def get_command_args():
  return sys.argv

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
  

# Environment Variable setup


env_var_name = open("LostiaFiles/.ash_env_name").readlines()
env_var_value = open("LostiaFiles/.ash_env_value").readlines()

def add_new_env_var(name,value):
  global env_var_name
  global env_var_value
  if(name in env_var_name):
    return None
  if(name.replace(" ","") == ""):
    raise ValueError("Environment variable name cannot be empty")
  if(name.startswith(" ")):
    raise ValueError("Environment variable name cannot start with space")
  name = str(name)
  with open("LostiaFiles/.ash_env_name","a") as newData:
    newData.write("\n"+str(name))
    newData.close()
  with open("LostiaFiles/.ash_env_value","a") as newData:
    newData.write("\n"+str(value))
    newData.close()