
class WordStatistics(object):

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

    # this function is case-sensitive, not going to replace if the old word is lowercase
    def replacement(old_word, new_word, text):
        # include puncuations and whitespace
        exclusion = '''!()[]{};:'"\, <>./?@#$%^&*_~ \n\t'''
        start = 0
        while(True):
            index = text.find(old_word, start)
            if index < 0:
                break
            if (index - 1 < 0 or text[index - 1] in exclusion) and (index + len(old_word) + 1 > len(text) - 1 or text[index + len(old_word)] in exclusion):
                text = text.replace(old_word, new_word, 1)
            else:
                start = index + len(old_word)

        return text


    if __name__ == "__main__":
        # sample code
        file = open("text.txt", 'r')
        text = file.read()
        word_list = words(text)
        print('Words:', word_list)
        freq = wc(word_list)
        print('Unigue Word count frequency: ', freq)
        lines = line_count(text)
        print('Lines: ', lines)
        cnt = char_count(text)
        print('Char count: ', cnt)
        replaced = replacement('in', 'name', text)
        print('text before replacement: ' + text)
        print('text after replacement: ' + replaced)