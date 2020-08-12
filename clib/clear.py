import os
import sys
from command import end
def clear():
  print("\033c", end="\r")
clear()
print("Note: The password for root (systemadmin) is set to 'password' by default, access root by typing 'login systemadmin'")
end(sys.argv)