class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding = 'utf-8') as file:
                a = file.read().lower()
                all_words[i] = a.split()

        return all_words

    def find(self, word):
        dint = {}
        word = word.lower()
        a = self.get_all_words()
        for file_name, words in a.items():
            if word in words:
                dint[file_name] = words.index(word) + 1

                return dint




    def count(self, word):
        dirt = {}
        c = self.get_all_words()
        for file_names, words in c.items():
            if word.lower() in words:
                dirt[file_names] = words.count(word.lower())
                return dirt





w1 = WordsFinder('text.txt')
print(w1.get_all_words())

print(w1.find('TEXT'))
print(w1.count('FoR'))