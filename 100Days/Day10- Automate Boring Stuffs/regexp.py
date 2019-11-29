import re

phoneNumRegexp = re.compile(r'((\d\d\d)-(\d\d\d\d))')
mo = phoneNumRegexp.search('My number is 417-5106')
print(f'phone number found {mo.group()}')
print(f'area code found {mo.group(1)}')
print(f'main number {mo.group(2)}')

mox = phoneNumRegexp.findall('My phone number is 417-5106 and home number is 674-0688')
print(mox)


batRegex = re.compile(r'Bat(wo)?man')
batRegex2 = re.compile(r'Bat(man|mobile|copter)')
batRegex3 = re.compile(r'Bat(wo)*man')
batRegex4 = re.compile(r'Bat(wo)+man')

mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())


haRegExp = re.compile(r'(Ha){3}')
print(haRegExp.search('HaHaHaHa').group())