
"""
fileUnderReplacer.py
Mass replace "_" (underscores) to " " (spacebar) from file name in whole folder
file_1, file_2 => file 1, file 2
"""

import os
import glob
files = glob.glob('*_*')
for file in files:
    new_name = file.replace("_", " ")
    os.rename(file, new_name)
