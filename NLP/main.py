import A
import B
import C

import subprocess

subprocess.run(['python', 'A.py'], check=True)
subprocess.run(['python', 'B.py'], check=True)
subprocess.run(['python', 'C.py'], check=True)

#This is the code that executes all the python scripts needed to run