import shutil, os
import send2trash


f = open('text_file.txt', 'w')
f.write('abcdefg')
f.close()

os.chdir('C:\\Users\\hdargaye\\Desktop\\CodePlayground\\PyPlayground')
#os.mkdir('NewFolder')

src_file = 'C:\\Users\\hdargaye\\Desktop\\CodePlayground\\PyPlayground\\text_file.txt'
dest_folder = 'C:\\Users\\hdargaye\\Desktop\\CodePlayground\\PyPlayground\\NewFolder'
shutil.copy(src_file, dest_folder) # Copying to another directory
shutil.copy(src_file, 'another_text_file') # Renaming the file

# Moving files
shutil.move(src_file, dest_folder + '\\ asanothertext.txt')

# deleting files
#os.unlink(dest_folder + '\\ asanothertext.txt')
#shutil.rmtree(dest_folder) #remove the directory with all the files

os.chdir(dest_folder)
for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        #send2trash.send2trash(filename)
        print(filename)

