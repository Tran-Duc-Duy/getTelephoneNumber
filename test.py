import re
fileName = input()
#phone-numbers.txt
with open(fileName, 'r') as rf:
    str =rf.read()
    arr = re.findall("[+]\d+",str)
with open('out.txt', 'w') as wf:
    for text in arr:
        wf.write(text + '\n')

import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = ".\\platform\\"