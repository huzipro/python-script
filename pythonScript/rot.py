
"""
rot.py
Encrypt or decrypt text based from rot cipher
"""

wordSmall = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
wordLarge = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(n):
    print("Paste the text below:")
    unencrypted = input()
    answerList = []
    for item in unencrypted:
        for word in wordSmall:
            if item == word:
                item = 
        if item in wordSmall:
            item = wordSmall[x+n]
            item.append(answerList)
        elif item in wordLarge[x]:
            item = wordLarge[x+n]
            item.append(answerList)
        else:
            item.append(answerList)

def decrypt(arg):
    pass

if __name__ == "__main__":
    print("""Welcome to rot.py.
          1. Encrypt
          2. Decrypt""")
    answer = input("Select an option (1 or 2): ")
    if answer == "1":
        n = input("which rot do you want to convert?: ")
        encrypt(n)
