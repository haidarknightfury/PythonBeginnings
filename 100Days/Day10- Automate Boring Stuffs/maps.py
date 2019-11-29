birthdays = {
    'Haidar': '05/12/1995',
    'Baka': '05/12/1995'
}

# Print all keys
for k in birthdays.keys():
    print(k)

# Print all values
for v in birthdays.values():
    print(v)

for k, v in birthdays.items():
    print(f'{k}=> {v}')

print("Default Testing "+ birthdays.get('NoName','01/01/2000'))

while(True):
    name = str(input("Enter name :"))
    if name == '':
        break
    if name in birthdays:
        birthday = birthdays[name]
        print(f"{name}'s birthday is {birthday}")
    else:
        print(f"{name}'s birthday not present")
