#!usr/bin/env python
"""
namer.py
Select the option and let the program rename the files according to the option selected. The idea of this program is to compile all of the common repetitive task of renaming files. For example if the option for remove underscore (_) is 1 and the option to remove bracket is 2, you can use 2 command at once by typing "12".

Style Guide:
  var = using_underscore
  funct = camelCase
  comment = all lowercase
  multi-comment = Uppercase and lowercase
"""
import os
import glob

option = []

def bracket():
  files = glob.glob('*(*).txt')
  for file in files:
    new_name = file.replace("(", "")
    new_name2 = new_name.replace(")", "")
    print(new_name2)
    os.rename(file, new_name2)
    print("Bracket")

def underscore():
  files = glob.glob('*_*')
  for file in files:
    new_name = file.replace("_", " ")
    os.rename(file, new_name)
    print("Underscore")

# main program
def main():
  # program user interface
  print("""
    1. Bracket Remover
    2. Underscore Remover
  """)

  # option parser
  select = input("Option: ")
  for item in select:
    option.append(item) #pushing the option into the list
  for options in option: #executing each option in the list
    if options == "1": # calling the function name
      bracket()
      print("Command " + options + " success!")
    elif options == "2":
      underscore()
      print("Command " + options + " success!")
    else:
      print("Command " + options + " not found!")

if __name__ == '__main__':
  main()