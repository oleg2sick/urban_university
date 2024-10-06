class WordsFinder:

    file_names = []

    def __init__(self, *args):
        for arg in args:
            self.file_names.append(arg)

    def get_all_words(self):

        all_words = {}

        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as names:
                append_word = []
                for lines in names:
                    punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for p in punct:
                        if p in lines:
                            lines = lines.replace(p, '')
                    lines = lines.lower().split()
                    append_word.extend(lines)
                all_words[i] = append_word

        return all_words

    def find(self, word):

        find_word = {}
        self.word = word.lower()

        for name, words in self.get_all_words().items():
            if self.word in words:
                find_word[name] = words.index(self.word) + 1

        return find_word

    def count(self, word):

        word_counter = {}
        self.word = word.lower()

        for name, words in self.get_all_words().items():
            word_counter[name] = words.count(self.word)

        return word_counter



finder2 = WordsFinder('test.txt')
print(finder2.get_all_words()) 
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

