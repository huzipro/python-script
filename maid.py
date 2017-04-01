
"""
maid.py
My personal assistant
"""

import winsound

# sound
def initSound(): winsound.PlaySound('./maid_files/init.wav', winsound.SND_FILENAME)
def blipSound(): winsound.PlaySound('./maid_files/blip.wav', winsound.SND_FILENAME)

def help():
  print("""
The thing that I understand:
help
backup
""")

# features
def backup():
  print('backuped')
  blipSound()

# start the program
def main():
  initSound()
  while True:
    command = input('\nWhat will be your pleasure today sir?\n>>> ').split(' ')[0]
    if command == 'help':
      help()
    elif command == 'backup':
      backup()
    else:
      print('I don\'t understand that command sir')
      main()
    print('Understood.')

if __name__ == '__main__':
  main()