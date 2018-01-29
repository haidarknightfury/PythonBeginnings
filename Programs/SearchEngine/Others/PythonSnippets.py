# Write Python code that assigns to the
# variable url a string that is the value
# of the first URL that appears in a link
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url',
# and therefore still prints the same thing.

# page = contents of a web page
page = ('<div id="top_bin"><div id="top_content" class="width960">'
        '<div class="udacity float-left"><a href="http://udacity.com">')
tag = page.find('<a href=')
start_link = page.find('"',tag) + 1
end_link = page.find('"',start_link)
url = page[start_link:end_link]
print(url)


# Number of hours in 7 week
print (7*7*24)

text = "all zip files are zipped"

# ENTER CODE BELOW HERE
first_occurrence = text.find('zip')
second_occurrence = text.find('zip',first_occurrence+1)
print(second_occurrence)

#ROUND UP

x = 3.54159

#ENTER CODE BELOW HERE
xStr = str(x)
dot = xStr.find('.')
roundup = xStr[0:dot]
nextChar = xStr[dot+1]
value = int(roundup)
if(int(nextChar)>4):
    value = value +1
print(value)


# find last occurence of a string
def find_last(str, to_find):
    i = -1
    last = -1
    while i < len(str):
        if(str[i] == to_find):
            last = i
        i = i + 1
    return last

# Number of stamps in 5,2 and 1 coins
def stamps(n):
    five=0
    two=0
    one =0
    while(n>=5):
        n=n-5
        five=five+1
    while(n>=2):
        n=n-2
        two=two+1
    while(n>=1):
        n=n-1
        one=one+1
    return five,two,one


#Range of a set

def min(a, b, c):
    if (a < b):
        if (a < c):
            return a
    if (b < a):
        if (b < c):
            return b
    else:
        return c


def max(a, b, c):
    if (a > b):
        if (a > c):
            return a
    if (b > a):
        if (b > c):
            return b
    else:
        return c


def set_range(a, b, c):
    mn = min(a, b, c)
    mx = max(a, b, c)
    return mn - mx


print set_range(10, 4, 7)


# Test palindrome
word = madam
is_palindrome = word  == word[::-1] # reverse


# LOOP
def find_element(p,v):
    if v in p:
        return p.index(v)
    else:
        return -1
