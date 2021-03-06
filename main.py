import time
from time import sleep
import os
import sys
os.system("clear")
print("Lostia startup")

def logoutcurrentuser():
  userdata = open("LostiaFiles/user.data","w")
  userdata.write("guest")
  userdata.close()

def validatelogofile():
  try:
    print('Searching for File "Logo.loslogo" Status: [Searching]', end='\r')
    arr = os.listdir("LostiaFiles/")

    for i in arr:

      if(i == "Logo.loslogo"):
        return print('Searching for File "Logo.loslogo" Status:     [Found]')
      else:
        pass
    print("                                                               ")
    print("[ERROR] Logo file missing. Aborting")
    quit()
  except:
    print("[ERROR] Failed to validate files, aborting.")
    quit()

def validateerrorfile():
  try:
    print('Searching for File "Lostiaerrorcritical.loserror" Status: [Searching]', end='\r')
    arr = os.listdir("LostiaFiles/")

    for i in arr:

      if(i == "Lostiaerrorcritical.loserror"):
        return print('Searching for File "Lostiaerrorcritical.loserror" Status:     [Found]')
      else:
        pass
    print("                                                               ")
    print("[ERROR] Error file missing. Aborting")
    quit()
  except:
    print("[ERROR] Failed to validate files, aborting.")
    quit()

def validatecoreconffile():
  try:
    print('Searching for File "CoreConf.config" Status: [Searching]', end='\r')
    arr = os.listdir("LostiaMain/")

    for i in arr:

      if(i == "CoreConf.config"):
        return print('Searching for File "CoreConf.config" Status:     [Found]')
      else:
        pass
    print("                                                               ")
    print("[ERROR] Error file missing. Aborting")
    quit()
  except:
    print("[ERROR] Failed to validate files, aborting.")
    quit()


def validatemoduleconffile():
  try:
    print('Searching for File "ModuleConf.config" Status: [Searching]', end='\r')
    arr = os.listdir("LostiaMain/")

    for i in arr:

      if(i == "ModuleConf.config"):
        return print('Searching for File "ModuleConf.config" Status:     [Found]')
      else:
        pass
    print("                                                               ")
    print("[ERROR] Error file missing. Aborting")
    quit()
  except:
    print("[ERROR] Failed to validate files, aborting.")
    quit()


def validatecmdhandlerfile():
  try:
    print('Searching for File "commandhandler.py" Status: [Searching]', end='\r')
    arr = os.listdir("LostiaMain/")

    for i in arr:

      if(i == "commandhandler.py"):
        return print('Searching for File "commandhandler.py" Status:     [Found]')
      else:
        pass
    print("                                                               ")
    print("[ERROR] Error file missing. Aborting")
    quit()
  except:
    print("[ERROR] Failed to validate files, aborting.")
    quit()






def LogoRender():
  logo = open("LostiaFiles/Logo.loslogo")
  for i in logo:
    print(i)
    time.sleep(0.2)
  os.system("clear")
  return None


os.system("clear")


validatelogofile()
validatecmdhandlerfile()
validatecoreconffile()
validateerrorfile()
validatemoduleconffile()

print("Startup complete! Launching Lostia Professional")
time.sleep(1)
os.system("clear")
LogoRender()
logoutcurrentuser()

time.sleep(1)
os.system("clear")
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

print("Lostia Software, Ash\nVersion 1.4.1, Alpha C")
os.system("python LostiaMain/commandhandler.py")


#Why can't you eliminate Satan from Linux? Because 666 isn't executable.