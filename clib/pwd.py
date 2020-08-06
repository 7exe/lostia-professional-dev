from command import end
import os
import sys
loggedInUser = open("LostiaFiles/user.data").read()
if(loggedInUser == "guest"):
  split = sys.argv[0].split("/")
  lenSplit = len(split)
  print(split[lenSplit-1].replace(".py","")+": PERMISSION DENIED.")
  end(sys.argv)
if(loggedInUser == "systemadmin"):
  dir = open("LostiaFiles/current.directory").read().replace("LostiaFiles/","")
else:
  dir = open("LostiaFiles/current.directory").read().replace("LostiaFiles/root/","")
print(dir)
end(sys.argv)