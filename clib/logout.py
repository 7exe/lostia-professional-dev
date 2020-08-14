import sys
from command import *

currentdata = open("LostiaFiles/user.data").read()

if(currentdata != "guest"):
  changedata = open("LostiaFiles/user.data","w")
  changedata.write("guest")
  changedata.close()
  print("Successfully logged out!")
  isLoggedIn = False
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

  #Guess i should put a reference here


  end(sys.argv)
else:
  print("Cannot logout from user 'guest'")
  end(sys.argv)
