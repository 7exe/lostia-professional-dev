import os
from command import end
import sys



users = open("LostiaFiles/keychain.keychain").readlines()


if("-l" in sys.argv):
  title1 = "\033[34mUser"
  title2 = "Permission"
  title3 = "Created\033[39m"
  print("%-20s %-20s %s" %(title1,title2,title3))


  if("-sh" in sys.argv):
    for user in users:
      currentUser = user.split("/")[1]
      currentPerm = user.split("/")[4]
      currentCreated = user.split("/")[6]
      print("%-15s %-20s %s" %(currentUser,currentPerm,currentCreated))
    end(sys.argv)
  else:
    for user in users:
      if(user.split("/")[5] == "hidden"):
        pass
      else:
        currentUser = user.split("/")[1]
        currentPerm = user.split("/")[4]
        currentCreated = user.split("/")[6]
        print("%-15s %-20s %s" %(currentUser,currentPerm,currentCreated))
    end(sys.argv)

if("-sh" in sys.argv):
  printOutput = ""
  for user in users:
    printOutput += user.split("/")[1]+", "
  print(printOutput)
  end(sys.argv)
else:
  printOutput = ""
  for user in users:
    if(user.split("/")[5] == "hidden"):
      pass
    else:
      printOutput += user.split("/")[1]+", " 
  print(printOutput)
      
  end(sys.argv)