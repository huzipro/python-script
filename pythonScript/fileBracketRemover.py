
"""
fileBracketRemover.py
Mass remove "()" (brackets) from file name in whole folder
file (1), file (2) => file 1, file 2
"""

import os
import glob
files = glob.glob('*(*).txt')
for file in files:
    new_name = file.replace("(", "")
    new_name2 = new_name.replace(")", "")
    os.rename(file, new_name2)
