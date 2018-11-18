
def getFileSuffix(filename, with_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if with_dot else pos + 1
        return filename[index:]
    else:
        return ' '


if __name__ == '__main__':
    print(getFileSuffix('hai.dar.txt', True))
