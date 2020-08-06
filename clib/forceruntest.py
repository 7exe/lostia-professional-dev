from command import force_run_command, end
import time
from time import sleep
import sys

count = 0
force_run_command("install ./test2.zip -k")
force_run_command("install ./tree_v2.zip -k")
force_run_command("install ./lostiatest.zip -k")
force_run_command("thiscmddoes notexist -k")
end(sys.argv)