import pyperclip

clipboardTxt = pyperclip.paste()
lines = clipboardTxt.split('\n')
for i in range(len(lines)):
    lines[i] = '* '+ lines[i]
result = '\n'.join(lines)
pyperclip.copy(result)