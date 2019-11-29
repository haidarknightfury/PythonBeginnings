def analyse(content, chr):
    count = 0
    for character in content:
        if(character == chr):
            count += 1
    return (count / len(content)) * 100


def analyse_file(alpha):
    result = 0
    with open('text_file.txt') as f:
        content = f.read()
        result = analyse(content, alpha)
    return result


if __name__ == "__main__":
    percent = analyse('aabbcc', 'a')
    print(percent)
    percent = analyse_file('a')
    print(percent)
