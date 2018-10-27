# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    if s=='':
        return True;
    else:
        if(s[0]==s[len(s)-1]):
            return is_palindrome(s[1:(len(s)-1)])
        else:
            return False