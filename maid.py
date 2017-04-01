import time
import winsound

initS = winsound.PlaySound('./maid_files/init.wav', winsound.SND_FILENAME)
blipS = winsound.PlaySound('./maid_files/blip.wav', winsound.SND_FILENAME);

def backup:
  pass

def main():
  initS

if __name__ == '__main__':
  main()