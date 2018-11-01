import getpass

username = str(input('Enter username'))
password = getpass.getpass('Enter password')

if username == 'admin' and password == '123456':
    print('Authentication Success')
else:
    print('Authentication fail')