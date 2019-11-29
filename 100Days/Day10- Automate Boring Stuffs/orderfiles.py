import shutil, os, sys

def moveFiles(destFolder, extension):
    """
      method to move files in a directory  with a specific extensions to a destFolder

    """
    if destFolder not in os.listdir():
        os.mkdir(destFolder)
    for fileName in os.listdir():
        if fileName.lower().endswith(extension):
            try:
                shutil.move(fileName, destFolder)
                print('%s moved to %s' %(fileName,destFolder))
            except Exception as ex:
                print('%s not moved to %s due to %s' %(fileName,destFolder, ex))


if __name__ == "__main__":
    arguments = sys.argv[1:]
    assert len(arguments) == 2, "Wrong number of arguments"
    moveFiles(arguments[0],arguments[1])