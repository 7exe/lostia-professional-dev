import os
import sys
from command import end
def clear():
  print("\033c", end="\r")
clear()
end(sys.argv)