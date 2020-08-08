from command import end
import sys

historyAsArray = open("LostiaFiles/.gripple_history").readlines()

lineCount = 0

if("-c" in sys.argv):
  open("LostiaFiles/.gripple_history","w").close()
else:
  if(len(sys.argv)>2):
    if(sys.argv[1] == "-s"):
      for command in historyAsArray:
        lineCount += 1
        if(command.startswith(sys.argv[2])):
          calc = 4-len(str(lineCount))
          string = " "*calc
          print(string+"\033[38;5;242m"+str(lineCount)+"\033[39m  "+command.replace("\n","").replace(sys.argv[2].replace(" ",""),"\033[38;5;1m"+sys.argv[2].replace(" ","")+"\033[39m"))
  else:
    for command in historyAsArray:
      lineCount += 1
      calc = 4-len(str(lineCount))
      string = " "*calc
      print(string+"\033[38;5;242m"+str(lineCount)+"\033[39m  "+command.replace("\n",""))


end(sys.argv)

