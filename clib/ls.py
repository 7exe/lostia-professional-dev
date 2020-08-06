from command import end
import sys
import os
import platform
def creation_date(path_to_file):
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

fileType1 = ["sh","csh","py","pl"]

fileType2 = ["tar","tgz","arj","taz","lzh","lzma","tlz","txz","zip","z","Z","dz","gz","lz","xz","bz2","bz","tbz","tbz2","tz","deb","rpm","jar","war","ear","sar","rar","ace","zoo","cpio","7z","rz"]

fileType3 = ["jpg","jpeg","gif","bmp","pbm","pgm","ppm","tga","xbm","xpm","tif","tiff","png","svg","svgz","mng","pcx","mov","mpg","mpeg","m2v","mkv","webm","ogm","mp4","m4v","mp4v","vob","qt","nuv","wmv","asf","rm","rmvb","flc","avi","fli","flv","gl","dl","xcf","xwd","yuv","cgm","emf","axv","anx","ogv","ogx"]

fileType4 = ["aac","au","flac","mid","midi","mka","mp3","mpc","ogg","ra","wav","axa","oga","spx","xspf"]

fileType5 = ["bak","save"]
def is_sticky(path):
    return os.stat(path).st_mode


loggedInUser = open("LostiaFiles/user.data").read()
if(loggedInUser == "guest"):
  split = sys.argv[0].split("/")
  lenSplit = len(split)
  print(split[lenSplit-1].replace(".py","")+": PERMISSION DENIED.")
  end(sys.argv)

def getListOfFiles(dirName):
  listOfFile = os.listdir(dirName)
  allFiles = list()
  for entry in listOfFile:
      fullPath = os.path.join(dirName, entry)
      allFiles.append(fullPath)
  return allFiles     

currentDir = open("LostiaFiles/current.directory").read()
count = 0
endLs = ""
if(len(sys.argv) > 2):
  print("O")
  if(sys.argv[1] == "-la"):
    print("O")
    for I in getListOfFiles(currentDir):
      print(I)
      print("O")
      if(os.path.isdir(I)):
        if(I == "LostiaFiles/root/home"):
          print("%-10s %s" %(creation_date(I)+"\033[38;5;242m"+I.replace(currentDir,"")+"\033[39m"))
        else:
          print("%-10s %s" %(creation_date(I)+"\033[34m"+I.replace(currentDir,"")+"\033[39m"))

      else:
        split = I.split(".")
        if(split[-1] in fileType1):
          print("%-10s %s" %(creation_date(I)+"\033[38;5;200m"+I.replace(currentDir,"")+"\033[39m"))
        elif(split[-1] in fileType2):
          print("%-10s %s" %(creation_date(I)+"\033[38;5;196m"+I.replace(currentDir,"")+"\033[39m "))
        elif(split[-1] in fileType3):
          print("%-10s %s" %(creation_date(I)+"\033[38;5;98m"+I.replace(currentDir,"")+"\033[39m "))
        elif(split[-1] in fileType4):
          print("%-10s %s" %(creation_date(I)+"\033[38;5;38m"+I.replace(currentDir,"")+"\033[39m "))
        elif(split[-1] in fileType5):
          print("%-10s %s" %(creation_date(I)+"\033[38;5;220m"+I.replace(currentDir,"")+"\033[39m "))
        if(split[-1] not in fileType1 and split[-1] not in fileType2 and split[-1] not in fileType3 and split[-1] not in fileType4 and split[-1] not in fileType5):
          print("%-10s %s" %(creation_date(I)+I.replace(currentDir,"")))
if(len(sys.argv)<2):
  for I in getListOfFiles(currentDir):
    count+=1
    if(count == 5):
      print(endLs)
      endLs = ""
    if(os.path.isdir(I)):
      if(I == "LostiaFiles/root/home"):
        endLs+=" \033[38;5;242m"+I.replace(currentDir,"")+"\033[39m"
      else:
        endLs+=" \033[34m"+I.replace(currentDir,"")+"\033[39m"
    else:
      split = I.split(".")
      if(split[-1] in fileType1):
        endLs+=" \033[38;5;200m"+I.replace(currentDir,"")+"\033[39m"
      elif(split[-1] in fileType2):
        endLs+=" \033[38;5;196m"+I.replace(currentDir,"")+"\033[39m "
      elif(split[-1] in fileType3):
        endLs+=" \033[38;5;98m"+I.replace(currentDir,"")+"\033[39m "
      elif(split[-1] in fileType4):
        endLs+=" \033[38;5;38m"+I.replace(currentDir,"")+"\033[39m "
      elif(split[-1] in fileType5):
        endLs+=" \033[38;5;220m"+I.replace(currentDir,"")+"\033[39m "
      if(split[-1] not in fileType1 and split[-1] not in fileType2 and split[-1] not in fileType3 and split[-1] not in fileType4 and split[-1] not in fileType5):
        endLs+=" "+I.replace(currentDir,"")

print(endLs)
end(sys.argv)
