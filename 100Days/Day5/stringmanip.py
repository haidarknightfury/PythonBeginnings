str1 = 'Hello World !!'
print(len(str1))
print(str1.capitalize())
print(str1.upper())
print(str1.find('or'))  # 7
print(str1.find('shit')) #1

# index same as find but throws exception if not found
# print(str1.index('or'))
# print(str1.index('shit'))

print(str1.startswith('of')) #false
print(str1.startswith('Hell')) #true

print(str1.endswith('!!'))
print(str1.center(50, '*')) 
# ******************Hello World !!******************
print(str1.rjust(50, ' ')) # Space to the right

str2 = 'abc123456'
print(str2[2]) #c
print(str2[2:5]) # c12
print(str2[2:]) # c123456


print(str2[2::2]) # Start from 2nd position , Skip 2
print(str2[2::3]) # Start from 2nd position, Skip 3
print(str2[::2]) # Every 2nd position(
print(str2[::-1]) # Start from -1 Position i.e Reverse String
print(str2[-3:-1]) # '-' take from left

print(str2.isdigit()) #false
print(str2.isalpha()) #false
print(str2.isalnum()) #true

str3 = '  Jack Bauer  '
print(str3.strip()) #remove trailing spaces