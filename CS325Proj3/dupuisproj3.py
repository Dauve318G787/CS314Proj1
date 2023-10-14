import os

parentDir = os.getcwd()

os.chdir(parentDir)
os.chdir("module_1")

with open('projectIntro.py', 'r') as projectIntro:

    code = projectIntro.read()
    exec(code)

os.chdir(parentDir)
os.chdir("module_2")

with open('getRawData.py', 'r') as getRawData:

    code = getRawData.read()
    exec(code)
 
os.chdir(parentDir)
os.chdir("module_3")

with open('getProcessedData.py', 'r') as getProcessedData:

    code = getProcessedData.read()
    exec(code)










