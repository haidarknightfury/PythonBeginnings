import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\hdargaye\\Desktop\\CodePlayground\\PyPlayground'):
    print('The current folder is %s' %folderName)

    for subfolder in subfolders:
        print('subfolder of  %s is  %s' %(folderName, subfolder))

        for filename in filenames:
            print ('file in %s is %s' %(subfolder, filename))

        print('')