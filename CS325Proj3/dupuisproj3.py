import os

parentDir = os.getcwd()

os.chdir(parentDir)
os.chdir("projectIntro")

with open('projectIntro.py', 'r') as projectIntro:

    code = projectIntro.read()
    exec(code)

os.chdir(parentDir)
os.chdir("getRawData")

with open('getRawData.py', 'r') as getRawData:

    code = getRawData.read()
    exec(code)
 
os.chdir(parentDir)
os.chdir("getProcessedData")

with open('getProcessedData.py', 'r') as getProcessedData:

    code = getProcessedData.read()
    exec(code)










