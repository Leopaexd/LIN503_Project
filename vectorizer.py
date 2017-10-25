# Author: Oliver Glant
# Generates feature vectors for posts, using a dictionary

import time

class Vectorizer(object):

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.vector_size = len(dictionary) #To avoid having the for loop access the whole dictionary for each post
        print("Vectorizer initialized")
        self.appending_time = 0
        self.word_counting_time = 0

    def vectorize(self, post):
        #Returns a feature vector representing input post, based on input dictionary
        vector = []
        start = time.time()
        for _ in range(self.vector_size):
            vector.append(0) #Ensures vector begins as null vector with correct dimensionality
        self.appending_time += time.time()-start
        start = time.time()
        for word in post:
            vector[self.dictionary[word]]+=1
        self.word_counting_time += time.time()-start
        return vector