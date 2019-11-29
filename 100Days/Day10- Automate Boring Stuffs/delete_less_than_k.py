lists = [1,1,1,1,2,2,2,3,3,2,1,3,2,2]
res = [x for x in lists if lists.count(x) >3]
print(res)