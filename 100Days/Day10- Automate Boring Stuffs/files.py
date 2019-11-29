import os

# Looping and joining files using os.path.join
myFiles = ['haidar.txt', 'courses.txt']
for file in myFiles:
    print(os.path.join('C:\\Users\hdargaye\Documents', file))

# Current working directory
parentDir = os.getcwd()
print(parentDir)

# Creating a directory
try:
    os.mkdir(os.path.join(os.getcwd(), 'NewFolder'))
except FileExistsError:
    print(f'file already exists')


## Change directory
os.chdir(os.path.join(os.getcwd(),'skeleton'))
print(os.getcwd())


helloFile = open(os.path.join(parentDir,'NewFolder','hello.txt'))
helloFileContent = helloFile.read()
print(helloFileContent)
helloFile.close()

helloFile = open(os.path.join(parentDir,'NewFolder','hello.txt'))
lines = helloFile.readlines()
print(lines)
helloFile.close()