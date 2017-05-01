
"""
genHtml.py
Generate HTML boilerplate
"""

import os
from sys import argv
from time import sleep

# Generate Folders
os.makedirs('css')
os.makedirs('js')
os.makedirs('img')

# Create js file
os.system('cd js/ && touch main.js')
os.system('cd css/ && touch style.css')

# Generate HTML
with open('index.html', 'w') as f:
    f.write("""<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>title</title>
    <link rel="stylesheet" href="style.css" type="text/css">
</head>

<body>


    <script src="js/main.js"></script>
</body>

</html>""")

# Self-destruct if the file in everywhere else
if os.getcwd() != 'D:\\PROGRAMMING\\git\\python-script':
    print('EX')
    time.sleep(0.5)
    print('  PLOOOSION!!!')
    remove(argv[0])
else:
    pass
