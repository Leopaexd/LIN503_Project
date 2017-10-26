# Author: Oliver Glant
# Classifier for forum posts, using Naive Bayes

from sklearn import naive_bayes
from scipy import sparse
import numpy as np
import time

class Classifier(object):
    def __init__(self,categorized_training_vectors): #initializes and fits classifier to training data
        print("Classifier initialized")
        self.bayes = naive_bayes.MultinomialNB()
        start = time.time()
        vectors_labels = self.Vectors_and_labels(categorized_training_vectors)
        vectors = vectors_labels[0]
        labels = vectors_labels[1]

        print("Fitting training data...")
        self.bayes.fit(vectors, labels)
        print("Training data fitted in","%.2f" % (time.time()-start)," seconds")

    def evaluate(self,categorized_testing_vectors):
        print("Evaluating classifier...")
        hits = 0
        total = 0
        vectors_labels = self.Vectors_and_labels(categorized_testing_vectors)
        testing_vectors = vectors_labels[0]
        testing_labels = vectors_labels[1]
        predicted_labels = self.bayes.predict(testing_vectors)
       # for vector in testing_vectors:
       #     predicted_labels.append(self.bayes.predict(vector))
        for label in predicted_labels:
            total += 1
            if predicted_labels[label] == testing_labels[label]:
                hits += 1

        print(hits," hits out of total: ", total, ". Hit-rate: ", (hits/total))

    def Vectors_and_labels (self,categorized_vectors):
        #Takes a list of feature matrices by category and returns matrices in index 0 and their labels in index 1
        vectors = []
        labels = []
        i = -1
        for category in categorized_vectors:
            i += 1
            vectors.append(category) #Appends matrix of vectors
            for vector in range(category.shape[0]):
                labels.append(i)
        vectors_labels = [sparse.vstack(vectors), labels] #All separate feature matrices are stacked vertically to form one large
        return vectors_labels