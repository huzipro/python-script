import shutil

# Important files in ~
dotFiles = ['C:\\Users\\AFFAN\\.bash_history',
            'C:\\Users\\AFFAN\\.bash_profile',
            'C:\\Users\\AFFAN\\.bashrc',
            'C:\\Users\\AFFAN\\.gitconfig',
            'C:\\Users\\AFFAN\\.gitignore_global',
            'C:\\Users\\AFFAN\\.minttyrc',
            'C:\\Users\\AFFAN\\.vimrc',]

for file in dotFiles:
    try:
        # Create the folder first
        # The folder is not relative path because I use this as an alias
        # shutil.copy2(file, './backupFiles/dotFiles/')
        shutil.copy2(file, 'D:\\PROGRAMMING\\git\\python-script\\backupFiles\\dotFiles')
    except PermissionError:
        print("Error occured: " + PermissionError)