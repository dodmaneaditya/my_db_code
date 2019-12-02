import shutil
dirPath = 'D:\\users\\40101390-old\\CWC -  CoWorking Capitals\\AAS_Model';
# Delete all contents of a directory using shutil.rmtree() and  handle exceptions
try:
    shutil.rmtree(dirPath)
except:
    print('Error while deleting directory')