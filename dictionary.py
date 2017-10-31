# Author: Oliver Glant
# Index words from a list of files and create a dictionary where each word is assigned an integer

import time


class Dictionary(object):

    def __init__(self):
        self.dictionary = dict()
        print("Dictionary created")

    def index_words(self, post_array):
        start = time.time()
        print("Indexing words")
        for post in post_array:
            for word in post:
                if word not in self.dictionary:
                    self.dictionary[word] = len(self.dictionary)
        time_elapsed = time.time() - start
        print("Indexing completed in ", ("%.2f" % time_elapsed), "seconds")

    def clear(self):
        self.dictionary.clear()
