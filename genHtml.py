
"""
genHtml.py
Generate HTML boilerplate
"""

import os
from sys import argv
from time import sleep

# Generate folders
os.makedirs('css')
os.makedirs('js')
os.makedirs('img')

# Create main.js file
os.system('cd js/ && touch main.js')
os.system('cd css/ && touch style.css')

# Generate index.html file
with open('index.html', 'w') as f:
    f.write("""<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>title</title>
    <link rel="stylesheet" href="reset.css" type="text/css">
    <link rel="stylesheet" href="style.css" type="text/css">
</head>

<body>
    
    <script src="js/main.js"></script>
</body>

</html>""")

# Generate reset.css
with open('css/reset.css', 'w') as f:
    f.write('abbr,article,aside,audio,blockquote,body,code,div,em,fieldset,footer,form,h1,h2,h3,h4,h5,h6,header,html,iframe,img,label,legend,li,nav,object,ol,p,pre,section,small,span,strong,sub,sup,table,tbody,td,tfoot,th,thead,time,tr,ul,video{margin:0;padding:0;border:0;font-size:100%;font-weight:inherit;vertical-align:baseline;background:0 0}input[type=checkbox],th{vertical-align:bottom}article,aside,figure,footer,header,nav,section{display:block}html{box-sizing:border-box;overflow-y:scroll}*,:after,:before{box-sizing:inherit}img,object{max-width:100%}ul{list-style:none}table{border-collapse:collapse;border-spacing:0}th{font-weight:700}td{font-weight:400;vertical-align:top}input,select{vertical-align:middle}input[type=radio]{vertical-align:text-bottom}strong{font-weight:700}button,input[type=file],label{cursor:pointer}button,input,select,textarea{margin:0;border:0}button::-moz-focus-inner{padding:0;border:0}')

# Self-destruct if the file in everywhere else
if os.getcwd() != 'D:\\PROGRAMMING\\git\\python-script':
    print('EX...')
    sleep(1)
    print("""MMMMMMMMMMMMMMMMMMMMMMMo   :dMMMMMMM/  :/// ./oMMMMNy:  -+MMMMMMMMMMMMMMMMMMMMMM
NMMMMMMMMMMMMMMMMMMMMMMo  .  /mMMMMo  -////`./+MMd+`   `/dMMMMMMMMMMMMMMMMMMMMMM
y::oymMMMMMMMMMMMMMMMMMo  /:`  +NMy  -/////``//o.  .-  :oMMMMMMMMMMMMMMMMMMMMMMM
MMh-  `-+sdNMMMMMMMMMMMo  ///:` `+  .//////.`:. `-:/` -/mMMMMMMMMMMMMMMMMMMMMMMM
MMMMd:      ./ohmMMMMMMo  /////-`  `///////-  .:///- ./oMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMd/  `..``  `-+ydNo  ///////-`////////:-/////:  :/mMMMMMMMMNmhyso+///dMMMMM
MMMMMMMMm/  `:/::-.`   `  :///////////////////////` -//yso/:-.`       ./yNMMMMMM
MMMMMMMMMMm+  `-/////:-.` ://////////////////////. `--  ```..----. `-/yNMMMMMMMM
MMMMMMMMMMMMNo` `-///////////////////////////////---::////////:. `-/yNMMMMMMMMMM
MMMMMMMMMMMMMMNo` `-////////////////////////////////////////:` .:/yNMMMMMMMMMMMM
MMMMMMMMMMMMMMms:   ./////////////////////////////////////-` .:/yNMMMMMMMMMMMMMM
MMMMMMMMMMNy/.  `.://///////////////////////////////////-``-//oNMMMMMMMMMMMMMMMM
MMMMMMMh+-    .://////////////////////////////////////:.``...   `.-:/+osyhdNMMMM
MMMMMMMMmyo/.   `..-:////////////////////////////////////////:::--.`   .-+yNMMMM
MMMMMMMMMMMMMMdyo.    .:///////////////////////////////////////:-` `.:+ymMMMMMMM
MMMMMMMMMMMMMMh+.  `-://////////////////////////////////////-.` .-:+ymMMMMMMMMMM
MMMMMMMMMMNy/`  .-://///////////////////////////////////:-` `.:/+ymMMMMMMMMMMMMM
MMMMMMMmo-  `.://///////:://////////////////////////////:` .://yMMMMMMMMMMMMMMMM
MMMMh+.    `.```````````` ://////.-///////////////:.://///:` .:/omMMMMMMMMMMMMMM
Ny+:--:::::::///////////- :////:`  `:////: `-:///// ```.-///:` .:/omMMMMMMMMMMMM
mddddmmmmmNNNNNNNNNMMMMy  :///- -/:. .:/:``:. `-///.`/:-.``.-::` .:/sNMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMh  -//.`:///+:` .` :///-` .-: -//+/:-.``..` .:/yNMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMd  -:`.///omMdo:` ./hMdy+/-.` `//MMmhs+:-.`   `:/yNMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMm  ``://+dMMMMMms-/yMMMMMmho/-.-/NMMMMMNmhs/-.` `:/hMMMMM""")
    print('                                                 PLOOOSION!!!')
    sleep(2)
    os.remove(argv[0])
else:
    pass
