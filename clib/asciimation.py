import time
from time import sleep 
import os
import sys
from command import end

def PlayAnimation(speed, files):
  try:
    Plane = open(files).read()
    PlaneFixed = Plane.split("END")
    os.system("clear")
    for I in PlaneFixed:
      print(I)
      time.sleep(speed)
      os.system("clear")
    print("Animation finished playing.")
    end()

  except:
    print("Failed to run animation")
  
if(len(sys.argv) > 1):
  pass
else:
  print("Missing arguments. Try asciimation help")
  end(sys.argv)
if(sys.argv[1] == "plane"):
  PlayAnimation(0.1,"LostiaFiles/plane.losanim")
elif(sys.argv[1] == "octobanana"):
  PlayAnimation(0.1,"LostiaFiles/octobanana.losanim")
elif(sys.argv[1] == "weirdanim"):
  PlayAnimation(0.1,"LostiaFiles/idk.losanim")
elif(sys.argv[1] == "help"):
  print("Asciimation Commands:\nplane - plane animation\noctobanana - animation credit to the creator of the animations")

if(sys.argv[1] != "plane" or sys.argv[1] != "octobanana" or sys.argv[1] != "weirdanim" or sys.argv[1] != "help"):
  print("Couldn't find example animation.")
  end(sys.argv)