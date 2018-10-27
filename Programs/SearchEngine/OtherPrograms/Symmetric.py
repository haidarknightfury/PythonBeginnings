# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.


def symmetric(lists):
   if lists == []:
        return False
   i = 0
   m = 0
   while i < len(lists):
        while(m < len(lists)):
            if lists[i][m] != lists[m][i]:
                return False
            m = m + 1
        i = i + 1
   return True


print symmetric([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 1]])
