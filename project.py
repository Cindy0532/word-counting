def words(text):
    # exclude -, since may have word such as three-year-old
    punc = '''!()[]{};:'"\, <>./?@#$%^&*_~'''
    for chr in text:
        if chr in punc:
            text = text.replace(chr, " ")
    words = [word.lower() for word in text.split()]

    return words


def wc(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


def line_count(text):
    if text == '':
        return 0
    cnt = 1
    for chr in text:
        if chr == '\n':
            cnt += 1

    return cnt


def char_count(text):
    return len(text)


if __name__ == "__main__":
    # sample code
    file = open("text.txt", 'r')
    text = file.read()
    word_list = words(text)
    print('Words:', word_list)
    freq = wc(word_list)
    print('Word count: ', freq)
    lines = line_count(text)
    print('Lines: ', lines)
    cnt = char_count(text)
    print('Char count: ', cnt)