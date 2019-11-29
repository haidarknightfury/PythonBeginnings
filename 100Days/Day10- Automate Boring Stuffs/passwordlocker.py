import pyperclip
import sys

PASSWORDS = {
    'email':'emailpassword',
    'blog': 'blogpassword'
}

if len(sys.argv) < 2:
    print(f'No arguments provided')
    sys.exit()
account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Retrieved password for {account}')
else:
    print(f'No account for {account}')