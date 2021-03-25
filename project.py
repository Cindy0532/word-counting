
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

if __name__ == "__main__":
    # sample code
    file = open("text.txt",'r')
    word_list = words(file.read())
    print(word_list)
    freq = wc(word_list)
    print(freq)

#






