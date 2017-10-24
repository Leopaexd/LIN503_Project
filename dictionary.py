# Author: Oliver Glant
# Index words from a list of files and create a dictionary where each word is assigned an integer

class Dictionary(object):
    dictionary = dict()
    print("Dictionary created")

    def IndexWords(self,post_array):
        print("Indexing words")
        for post in post_array:
            for word in post:
                if word not in self.dictionary:
                    self.dictionary[word] = len(self.dictionary)
        print("Indexing completed")