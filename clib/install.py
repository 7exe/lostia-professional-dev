import os
import sys
import zipfile
from command import end
cfgfixed = []

done = []

def reset():
  print("[Lostia Installer] Reverting")
  for I in done:
    try:
      os.remove(I)
      print("[Lostia Installer] Removed "+I)
    except:
      print("[Lostia Installer] Failed to remove "+I)

if(len(sys.argv) > 1):

  try:
    print("[Lostia Installer] Reading .cfg file of "+sys.argv[1])
    archive = zipfile.ZipFile(sys.argv[1], 'r')
    cfg = archive.read('cmd.cfg')
    cfgfixed = cfg.decode("utf-8").split(" ")
  except:
    print("[Lostia Installer] Failed to read .cfg file")
    end(sys.argv)
  
  for I in cfgfixed:
    try:
      print("[Lostia Installer] Installing command "+I)
      with zipfile.ZipFile(sys.argv[1]) as z:
        z.extract('clib/'+I+".py")
        done.append('clib/'+I+".py")
    except:
      print("[Lostia Installer] Failed to install command")
      reset()
      end(sys.argv)

    try:
      print("[Lostia Installer] Updating help")
      with zipfile.ZipFile(sys.argv[1]) as z:
        z.extract('LostiaHelp/'+I +".help")
        done.append('LostiaHelp/'+I +".help")
    except:
      print("[Lostia Installer] Failed to update help")
  print("[Lostia Installer] Done!")
  end(sys.argv)
else:
  print("install: must provide target")
  end(sys.argv)

