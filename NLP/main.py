import Analysis
import Labelling
import Sort

import subprocess

subprocess.run(['python', 'Analysis.py'], check=True)
subprocess.run(['python', 'Labelling.py'], check=True)

#This is the code that executes all the python scripts needed to run