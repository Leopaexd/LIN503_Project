# Author: Oliver Glant
# Generates feature vectors for posts, using a dictionary

import numpy as np
from scipy import sparse

class Vectorizer(object):

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.vector_size = len(dictionary) #To avoid having the for loop access the whole dictionary for each post
        print("Vectorizer initialized")

    def vectorize(self, post):
        #Returns a feature vector representing input post, based on input dictionary
        pre_vector = dict()
        for word in post:
            index = self.dictionary.get(word)
            if index in pre_vector:
                pre_vector[index]+=1
            else:
                pre_vector[index] = 1

        ####Vector CREATION####
        columns = [int(key) for key in pre_vector.keys()]
        row = [0 for entry in columns]
        data = [pre_vector.get(entry) for entry in columns]

        vector = sparse.csr_matrix((data,(row,columns)),shape = (1,self.vector_size))
        return vector