import os
import time


source = ['"C:\\Users\\hdargaye\\Documents\\Tech Specs"']
target_dir = 'C:\\Archieves'

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

today = target_dir+ os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Enter comment')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + comment.replace(' ','_')+ '.zip'

if not os.path.exists(today):
    os.makedirs(today)
    print('Created directory %s'%(today))

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
print('zip command is {0}'.format(zip_command))

if os.system(zip_command) == 0:
    print('successful')
else:
    print('failed')