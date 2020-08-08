import sys
from command import end
import os

historyAsArray = open("LostiaFiles/.gripple_history").readlines()

if(len(sys.argv)>1):
  if(int(sys.argv[1])<len(historyAsArray)):
    command = historyAsArray[int(sys.argv[1])-1]
    os.system("python clib/"+command.split(" ")[0].replace("\n","")+".py"+" "+command.replace(command.split(" ")[0],""))
    end(sys.argv)
  else:
    print("History line not found")
    end(sys.argv)
else:
  print("!: ! history line")
  end(sys.argv)