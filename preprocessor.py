# Author: Oliver Glant
# Pre-process Swedish forum posts
# Separate methods for tokenization and stemming to allow subclassing for other languages

from nltk.stem.snowball import SnowballStemmer
import time


class Preprocessor(object):
    stemmer = SnowballStemmer('swedish')

    stopwords = []
    with open('swedish_stopwords.txt', 'r') as file:
        for line in file:
            stopwords.append(line.strip('\n'))

    def preprocess(self, input_file):
        # returns a list containing all posts, each post is a list of stemmed words with stopwords removed
        start = time.time()
        print("Preprocessing ", input_file)
        with open(input_file) as file:  # Creates a list containing all tokenized posts
            tokenized_post_list = [self.tokenize(post) for post in file.readlines()]

        tokenized_post_list_no_stopwords = []
        for post in tokenized_post_list:
            tokenized_post_list_no_stopwords.append(self.remove_stopwords(post))

        processed_post_list = []
        for post in tokenized_post_list_no_stopwords:
            processed_post = []
            for word in post:
                processed_post.append(self.stem(word))  # replaces all words in all posts with their stem
            processed_post_list.append(processed_post)

        time_elapsed = time.time() - start
        print("Preprocessing completed in ", ("%.2f" % time_elapsed), "seconds")
        return processed_post_list

    def tokenize(self, post):
        return post.split()

    def remove_stopwords(self, post):
        output_post = []
        for word in post:
            if word not in self.stopwords:
                output_post.append(word)
        return output_post

    def stem(self, word):
        return self.stemmer.stem(word)
