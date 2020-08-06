from command import end
import time
from time import sleep
import sys
import psutil
import os

loggedInUser = open("LostiaFiles/user.data").read()

if(loggedInUser == "guest"):
  split = sys.argv[0].split("/")
  lenSplit = len(split)
  print(split[lenSplit-1].replace(".py","")+": PERMISSION DENIED.")
  end(sys.argv)

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def get_processes():
  print("\n\x1b[6;30;42m%-20s %-20s %-20s %-20s %-20s %s          \x1b[0m" %("NAME","PID","CPU%","MEM_HR","STATE","EXE"))
  for proc in psutil.process_iter():
    
    try:
        processName = proc.name()
        processID = proc.pid
        process = psutil.Process(processID)
        processMemUsage = sizeof_fmt(process.memory_info().rss)
        processCpuUsage = 0
        processCpuUsage = process.cpu_percent()
        processExe = process.exe()
        processState = process.status()
        print("%-20s %-20s %-20s %-20s %-20s %s" %(processName,processID,str(processCpuUsage),processMemUsage,processState,processExe))

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
def seconds_elapsed():
  return time.time() - psutil.boot_time()

def time_readable(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)
    
while True:
  try:
    os.system("clear")
    mem_percentage = 0
    mem_percentage = psutil.virtual_memory().percent
    visable2 = "|"*int(mem_percentage)
    calcedNumber2 = 100-int(mem_percentage)
    calcedEmpty2 = " "*calcedNumber2

    Mem1 = 0
    Mem2 = 0
    virtual_memory = psutil.virtual_memory()
    Mem1 = virtual_memory.available * 100 / virtual_memory.total
    Mem2 = virtual_memory.percent
    string2 = ""+str(sizeof_fmt(Mem2))+"/"+str(sizeof_fmt(Mem1))
    loadavrg1 = 0
    loadavrg2 = 0
    loadavrg3 = 0
    loadavrg1,loadavrg2,loadavrg3 = os.getloadavg() #\033[38;5;81m \033[38;5;51m

    cpu_percentage = 0
    cpu_percentage = psutil.cpu_percent()
    visable = "\033[39m"
    def add_user_to(cpu_perc_user):
      global visable
      for I in range(cpu_perc_user):
        visable+="\033[38;5;27m|\033[39m"
      
    def add_system_to(cpu_perc_user):
      global visable
      for I in range(cpu_perc_user):
        visable+="\033[38;5;1m|\033[39m"
    
    def add_nice_to(cpu_perc_user):
      global visable
      for I in range(cpu_perc_user):
        visable+="\033[38;5;11m|\033[39m"
    
    def add_io_to(cpu_perc_user):
      global visable
      for I in range(cpu_perc_user):
        visable+="\033[38;5;7m|\033[39m"
    def add_si_to(cpu_perc_user):
      global visable
      for I in range(cpu_perc_user):
        visable+="\033[38;5;201m|\033[39m"
        
    cpu_times_percent = psutil.cpu_times_percent() 
    cpu_user = int(round(cpu_times_percent.user))
    cpu_system = int(round(cpu_times_percent.system))
    cpu_iowait = int(round(cpu_times_percent.iowait))
    cpu_nice = int(round(cpu_times_percent.nice))
    cpu_softirq = int(round(cpu_times_percent.softirq))
    calcedEmptyNumber = 100 -(cpu_user + cpu_system + cpu_iowait + cpu_nice + cpu_softirq)
    calcedEmpty = "\x1b[8m|\x1b[0m"*calcedEmptyNumber
    string = ""+str(cpu_percentage)
    add_user_to(cpu_user)
    add_nice_to(cpu_nice)
    add_system_to(cpu_system)
    add_io_to(cpu_iowait)
    add_si_to(cpu_softirq)

    print("CPU ["+visable+calcedEmpty+"]"+" "+string+"%\033[39m")

    print("MEM ["+visable2+calcedEmpty2+"]"+" "+string2)
    print("\n\033[38;5;81mLoad Average: \033[39m"+str(loadavrg1)+" \033[38;5;51m"+str(loadavrg2)+" \033[38;5;81m"+str(loadavrg3)+"\033[39m")
    print("\033[38;5;81mUptime: \033[38;5;51m"+str(time_readable
    (round(seconds_elapsed()))+"\033[39m\n"))
    #print("Cpu Usage: \033[38;5;21muser \033[38;5;1msys \033[38;5;46midle")
    #cpu_time = psutil.cpu_times()
    #user = 0
    #user = cpu_time.percent.user
    #system = 0
    #system = cpu_time.system.percent
    #idle = 0
    #idle = cpu_time.idle.percent
    #print("\033[38;5;21m"+str(user)+" \033[38;5;1m"+str(system)+" \033[38;5;46m"+str(idle))

    get_processes()
    
    print("\n\x1b[48;5;249mCTRL+C\x1b[0m To quit")
    time.sleep(2)
  except KeyboardInterrupt:
    os.system("clear")
    end(sys.argv)
