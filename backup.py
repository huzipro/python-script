
"""
backup.py
This is the script to backup my files to ./backupFiles/ directory. I already put the backup folder inside .gitignore so it will not uploaded to the repository. If the files already exists. It will replace the files so it will update the backup files.
"""

import shutil

# Important files in ~
dotFiles = ['C:\\Users\\AFFAN\\.bash_history',
            'C:\\Users\\AFFAN\\.bash_profile',
            'C:\\Users\\AFFAN\\.bashrc',
            'C:\\Users\\AFFAN\\.gitconfig',
            'C:\\Users\\AFFAN\\.gitignore_global',
            'C:\\Users\\AFFAN\\.minttyrc',
            'C:\\Users\\AFFAN\\.vimrc',]

# Important files in D:\E-BOOK\Text\
textFiles = ['D:\\E-BOOK\\Text\\000webhost.jpg',
             'D:\\E-BOOK\\Text\\000webhost.txt',
             'D:\\E-BOOK\\Text\\Ammar Advice.txt',
             'D:\\E-BOOK\\Text\\Design.txt',
             'D:\\E-BOOK\\Text\\Dream.jpg',
             'D:\\E-BOOK\\Text\\FFmpeg.txt',
             'D:\\E-BOOK\\Text\\Gimp Tweak.txt',
             'D:\\E-BOOK\\Text\\Gmail.txt',
             'D:\\E-BOOK\\Text\\Linux Command.txt',
             'D:\\E-BOOK\\Text\\Linux Summary.txt',
             'D:\\E-BOOK\\Text\\Misc Account.txt',
             'D:\\E-BOOK\\Text\\Path.txt',
             'D:\\E-BOOK\\Text\\Universitas.txt',
             ]

for file in dotFiles:
    # The folder is not relative path because I use this as an alias
    # shutil.copy2(file, './backupFiles/dotFiles/')
    shutil.copy2(file, 'D:\\PROGRAMMING\\git\\python-script\\backupFiles\\dotFiles')

for file in textFiles:
    shutil.copy2(file, 'D:\\PROGRAMMING\\git\\python-script\\backupFiles\\textFiles')

print('\n  Backup success! no error occured.')