# Variables and Basic Arithmetic Operations

a = int(input(' a = '))
b = int(input(' b = '))
message = str(input('message ='))

print(' %d + %d = %d ' % (a, b, a + b))
print(' %d - %d = %d ' % (a, b, a - b))
print(' %d * %d = %d ' % (a, b, a * b))
print(' %d /%d = %f ' % (a, b, a / b))
print(' %d // %d = %d ' % (a, b, a // b))
print(' %d  %%  % d = %d ' % (a, b, a % b))
print(' %d ** %d = %d ' % (a, b, a ** b))
print(message)

# Checking type
c = 1 + 5j #Complex type
d = 'Hello world'
e = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


## Convertors
x = int(1) # To int
y = float(1.1) # to float
z = chr(74) # to character
s = ord(z) # to ascii


# Comparison operators

flag  = 1<2
flag2 = 3<4
print(flag is True)
print(flag is not False)

flag3 = flag or flag2
flag4 = flag and flag3







