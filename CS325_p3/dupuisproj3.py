#This file provides our tools with a roadmap for how it should execute. It starts by getting the current working directory and saves it as the
#parent directory. It then navigates to each module and runs the code in their source files.
#The source files execute in the following order: project intro, get raw data, get processed data.

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










