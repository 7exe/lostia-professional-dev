import sys
from command import end
import os

loggedInUser = open("LostiaFiles/user.data").read()
currentDir = open("LostiaFiles/current.directory").read()

def check_if_has_arguments():
  if(len(sys.argv)> 1):
    return True
  else:
    print("cd: .. or directory")
    end(sys.argv)

if(loggedInUser == "guest"):
  print("Permission Denied")
  end(sys.argv)

check_if_has_arguments()
if(loggedInUser != "systemadmin"):
  homeDir = "LostiaFiles/root/home/"+loggedInUser+"/"
else:
  homeDir = "LostiaFiles/root/"
if(".." not in sys.argv):
  if("-" not in sys.argv):
    if(os.path.isdir(currentDir+sys.argv[1])):
      open("LostiaFiles/current.directory","w").close()
      with open("LostiaFiles/current.directory","r+") as changeFile:
        changeFile.truncate(0)
        if("/" in sys.argv[1]):
          changeFile.write(currentDir+sys.argv[1])
        else:
          changeFile.write(currentDir+sys.argv[1]+"/")
        changeFile.close()
    else:
      print("Directory not found")
  else:
    with open("LostiaFiles/current.directory","r+") as changeFile:
        changeFile.truncate(0)
        changeFile.write(homeDir)
        changeFile.close()
else:
  if(currentDir != "LostiaFiles/root/home/"+loggedInUser+"/" and currentDir != "LostiaFiles/root/"):
    a = currentDir.split("/")
    for i in range(a.count("")):
      a.remove("")

    
    #  |           | Shouldn't fucking happen
    if (len(a) != 0):
        a.pop()
        Dir = ""
        count = 0
        for I in a:
      
          if(count != 0):
            Dir +="/"+I
          else:
            Dir += I
          count += 1
        Dir+="/"

        with open("LostiaFiles/current.directory","r+") as changeFile:
            changeFile.truncate(0)
            changeFile.write(Dir)
            changeFile.close()
  
end(sys.argv)