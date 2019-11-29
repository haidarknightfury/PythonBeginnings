myset = {1,2,3,4,5,6}
myset.add(-1)
print(myset)


res = list(map(lambda x: x*2, myset))
res_2 = list(map(lambda x: x*2 if x%2==0 else x*3, myset))
print(res)
print(res_2)

myset_1 = set(res)
print(myset_1)

myset_2 = set(res_2)
print(myset_2)

print('Union')
print(myset_1 | myset_2)
print(myset_1 & myset_2)
print(myset_1 - myset_2)



list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = ['a', 'b', 'c', 'd', 'e']
mixed = list(zip(list1,list2, list3))
print(mixed)

ls1,ls2,ls3 = zip(*mixed)
print(ls1)
print(ls2)