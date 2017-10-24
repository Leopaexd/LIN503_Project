# Author: Oliver Glant
# Generates feature vectors for posts, using a dictionary

class Vectorizer(object):
    @staticmethod
    def vectorize(self, post, dictionary):
        #Returns a feature vector representing input post, based on input dictionary
        vector = []
        for key in dictionary:
            vector.append(0) #Makes sure the vector is correct size and every index starts att zero
        for word in post:
            vector[dictionary[word]]+=1
        return vector