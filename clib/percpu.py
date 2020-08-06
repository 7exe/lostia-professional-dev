import os
import psutil
from command import end
import sys
import time
from time import sleep
while True:
  cpu = 0
  cpu = psutil.cpu_times_percent().user
  for i in range(psutil.cpu_count()):
    print("CPU "+str(i)+": "+str(cpu))
  time.sleep(2)
  os.system("clear")
end(sys.argv)