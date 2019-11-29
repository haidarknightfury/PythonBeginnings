import pprint

def characterCount():
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}
    for character in message:
        count.setdefault(character, 0)
        count[character] += 1
    pprint.pprint(count)
    print(count)

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
'Bob': {'ham sandwiches': 3, 'apples': 2},
'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests, item):
    sum = 0
    for k,v in allGuests.items():
        if k in guests:
            sum += v.get(item,0)
    return sum

if __name__ == "__main__":
    characterCount()
    total = totalBrought(['Alice', 'Bob'],'apples' )
    print(total)