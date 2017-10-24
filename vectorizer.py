# Author: Oliver Glant
# Generates feature vectors for posts, using a dictionary

class Vectorizer(object):

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.vector_size = len(dictionary) #To avoid having the for loop access the whole dictionary for each post
        print("Vectorizer initialized")

    def vectorize(self, post):
        #Returns a feature vector representing input post, based on input dictionary
        vector = []
        for _ in range(self.vector_size):
            vector.append(0) #Ensures vector begins as null vector with correct dimensionality
        for word in post:
            vector[self.dictionary[word]]+=1
        return vector