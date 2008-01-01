
"""
backup.py
This is the script to backup my files to ./backupFiles/ directory. I already put the backup folder inside .gitignore so it will not uploaded to the repository. If the files already exists. It will replace the files so it will update the backup files.
"""

import shutil

# Important files in ~
dotFiles = ["C:\\Users\\AFFAN\\.bash_history",
            "C:\\Users\\AFFAN\\.bash_profile",
            "C:\\Users\\AFFAN\\.bashrc",
            "C:\\Users\\AFFAN\\.gitconfig",
            "C:\\Users\\AFFAN\\.gitignore_global",
            "C:\\Users\\AFFAN\\.minttyrc",
            "C:\\Users\\AFFAN\\.vimrc",]

for file in dotFiles:
    # The folder is not relative path because I use this as an alias
    # shutil.copy2(file, "./backupFiles/dotFiles/")
    shutil.copy2(file, "D:\\PROGRAMMING\\git\\python-script\\backupFiles\\dotFiles")

print("\n  Backup success! no error occured.")
