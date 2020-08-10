from command import end
import sys

def echo():
  sysArr = sys.argv
  sysArr.pop(0)
  seperator = " "
  print(seperator.join(sysArr))
  end(sys.argv)

echo()