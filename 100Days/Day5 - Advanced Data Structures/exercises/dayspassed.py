def isLeap(year):
    return year % 4 == 0


def diffdays(year, month, date):
    daysofmonth = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], [
        31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]][isLeap(year)]
    total = 0
    for index in range(month - 1):
        total += daysofmonth[index]
    return total + date


if __name__ == '__main__':
    print(diffdays(2020, 12, 31))
