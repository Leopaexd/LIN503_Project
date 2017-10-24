# Author: Oliver Glant
# Pre-process Swedish forum posts
#Separate methods for tokenization and stemming to allow subclassing for other languages

from nltk.stem.snowball import SnowballStemmer

class PreProcessor(object):
    stemmer = SnowballStemmer('swedish')

    file = open('swedish_stopwords.txt','r')
    stopwords = []
    for line in file:
        stopwords.append(line.strip('\n'))
    file.close()

    def preprocess(self,input_file):
        #returns a list containing all posts, each post is a list of stemmed words with stopwords removed
        print("Preprocessing started")
        with open(input_file) as file:
            tokenized_post_list = [self.tokenize(post) for post in file.readlines()] #Creates a list containing all tokenized posts

        tokenized_post_list_no_stopwords = []
        for post in tokenized_post_list:
            tokenized_post_list_no_stopwords.append(self.remove_stopwords(post))

        processed_post_list = []
        for post in tokenized_post_list_no_stopwords:
            for word in post:
                processed_post_list.append(self.stem(word)) #replaces all words in all posts with their stem

        print("Preprocessing completed")
        return processed_post_list

    def tokenize(self,post):
        return post.split()

    def remove_stopwords(self,post):
        output_post = []
        for word in post:
            if word not in self.stopwords:
                #print("Removed: ",word)
                output_post.append(word)
        return output_post

    def stem(self,word):
        return self.stemmer.stem(word)