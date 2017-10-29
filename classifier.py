# Author: Oliver Glant
# Classifier for forum posts, using Naive Bayes

from sklearn import naive_bayes
from scipy import sparse
import time

class Classifier(object):
    def __init__(self): #initializes and fits classifier to training data
        print("Classifier initialized")
        self.bayes = naive_bayes.MultinomialNB()

    def train(self,categorized_training_vectors):
        start = time.time()
        vectors_labels = self.Vectors_and_labels(categorized_training_vectors)
        vectors = vectors_labels[0]
        labels = vectors_labels[1]

        print("Fitting training data...")
        self.bayes.fit(vectors, labels)
        print("Training data fitted in", "%.2f" % (time.time() - start), " seconds")


    def evaluate(self,categorized_testing_vectors):
        print("Evaluating classifier...")
        hits = 0
        total = 0
        vectors_labels = self.Vectors_and_labels(categorized_testing_vectors)
        testing_vectors = vectors_labels[0]
        testing_labels = vectors_labels[1]

        predicted_labels = self.bayes.predict(testing_vectors)
        label_list = ["Candy", "Physics, math and technology", "Nazism", "Pets", "Roleplaying and board games",
                      "Relationship advice", "Cannabis"]
        self.incorrect_list = []
        for i in range(len(predicted_labels)):
            total += 1
            if predicted_labels[i] == testing_labels[i]:
                hits += 1
            else:
                self.incorrect_list.append((str(i) + " " + label_list[predicted_labels[i]] + "\n"))
        with open("incorrect.txt","w") as file:
            for post in self.incorrect_list:
                file.write(post)

        print(hits," hits out of ", total, ". Hit-rate: ","%.2f" % (hits/total))

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

    def classify(self, unclassified_vectors):
        return self.bayes.predict(sparse.vstack(unclassified_vectors))