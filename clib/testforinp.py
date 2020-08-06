from command import end
import sys
import WConio
import end
import os
import time

while True:
  ans = WConio.getkey()
  print(ans)
  os.system("clear")
  if(ans == "y"):
    end(sys.argv)
  time.sleep(2)
