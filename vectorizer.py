# Author: Oliver Glant
# Generates feature vectors for posts, using a dictionary, takes a list of posts as inputs
# and generates a sparse matrix of feature vectors (csr_matrix)

from scipy import sparse

class Vectorizer(object):

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.vector_size = len(dictionary) #To avoid having the for loop access the whole dictionary for each post
        print("Vectorizer initialized")

    def vectorize(self, category):
        #Returns a feature vector representing input post, based on input dictionary
        columns = []
        rows = []
        data = []
        post_number = -1
        for post in category:
            post_number += 1
            word_count = len(post)
            for word in post:
                index = self.dictionary.get(word)
                if index is not None: #ignores words not found in dictionary
                    if index in columns:
                        data[columns.index(index)] += 1/word_count #relative word frequency instead of occurences
                    else:
                        columns.append(index)
                        rows.append(post_number)
                        data.append(1/word_count)
        vector = sparse.csr_matrix((data,(rows,columns)),shape = (post_number+1,self.vector_size))
        return vector