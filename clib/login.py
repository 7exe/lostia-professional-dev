from command import *
import sys
from getpass import getpass


userData = open("LostiaFiles/keychain.keychain").readlines()
currentUser = open("LostiaFiles/user.data").read()

def checkArgs():
  if(len(sys.argv)<2):
    print("login: username")
    return end(sys.argv)

def checkIfAlreadyLoggedIn():
  if(currentUser != "guest"):
    print("Cannot login when already logged in")
    end(sys.argv)
  else:
    return None

def login():
  checkArgs()
  checkIfAlreadyLoggedIn()
  count = 0
  for user in userData:
    if(sys.argv[1] == user.split("/")[2]):
      count = 1
      while count<4:
        try:
          askForPassword = getpass("[login] enter password for "+sys.argv[1]+": ")
        except UnicodeDecodeError:
          pass
        if(askForPassword == user.split("/")[3]):
          count = 4
          print("Successfully logged in!")
          userWriteNewData = open("LostiaFiles/user.data","w")
          userWriteNewData.write(user.split("/")[2])
          userWriteNewData.close()
          if(sys.argv[1] != "systemadmin"):
            changeHomeDir = open("LostiaFiles/current.directory","w")
            changeHomeDir.write("LostiaFiles/root/home/"+user.split("/")[2]+"/")
            changeHomeDir.close()
          else:
            changeHomeDir = open("LostiaFiles/current.directory","w")
            changeHomeDir.write("LostiaFiles/root/")
            changeHomeDir.close()
            currentUser = open("LostiaFiles/user.data").read()
            if(currentUser != "systemadmin"):
              if(currentUser != "guest"):
                homeDir = "LostiaFiles/root/home/"+currentUser+"/"
              else:
                homeDir = "None"
            else:
              homeDir = "LostiaFiles/root/"

            with open("LostiaFiles/.ash_env_name","w") as newData:
              newData.write("HOME")
              newData.close()

            with open("LostiaFiles/.ash_env_value","w") as newData:
              newData.write(homeDir)
              newData.close()

            with open("LostiaFiles/.ash_env_name","a") as newData:
              newData.write("\nUSER")
              newData.close()

            with open("LostiaFiles/.ash_env_value","a") as newData:
              newData.write("\n"+currentUser)
              newData.close()
          isLoggedIn = True
          return end(sys.argv)
        else:
          if(count != 3):
            print("Sorry, try again.")
          count+=1
    else:
      pass
  if(count!=0):
    print("login: 3 incorrect password attempts.")
  else:
    print("user not found")

  end(sys.argv)

login()