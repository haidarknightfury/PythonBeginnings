def has_duplicate_element(p):
   res = []
   for i in range(0, len(p)):
       for j in range(0, len(p)):
           if i != j and p[i] == p[j]:
               return True
   return False