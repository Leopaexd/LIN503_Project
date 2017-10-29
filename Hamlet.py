# Author: Oliver Glant
# Naive bayes classification of Swedish forum posts
# User interface

###Project modules###
from classifier import Classifier
from extractor import Extractor
from preprocessor import PreProcessor
from dictionary import Dictionary
import vectorizer
import dataset_divider

###Other modules ###
import time

###Global variables###
label_list = ["Candy","Physics, math and technology","Nazism","Pets","Roleplaying and board games","Relationship advice","Cannabis"]
######################

class naive_bayes_classifier(object):
    def __init__(self):
        self.Dictionary = Dictionary()
        self.Classifier = Classifier()
        self.PreProcessor = PreProcessor()
        self.set_categories()
        self.fit = False

    def set_categories(self):
        #Determines which labels are to be included
        self.categories = []
        print("\nDecide which categories to use:")
        for label in label_list:
            choice = ""
            while choice not in ["y","n"]:
                choice = input(("Include category: " + str(label_list.index(label) + 1) + "/" +
                                str(len(label_list)) + " " + label + "? (y/n)\n")).lower()
                if choice == "y":
                    self.categories.append(label_list.index(label)+1)
                if choice not in ["y","n"]:
                    print("You must input y or n.")

        if len(self.categories) == 0:
            print("Error! At least one category must be selected!")
            self.set_categories()

        print("You have selected the following categories:\n")
        for category in self.categories:
            print(str(category) + ". " + label_list[category-1] )

    def extract(self):
        #Extracts forum posts from .json-files generated by Scraper
        lines = []
        for category in self.categories:
            lines.append(
                Extractor.Extract(('flashback' + str(category) + '.json'), ('extracted' + str(category) + '.txt')))
            dataset_divider.Divider.Divide(('extracted' + str(category) + '.txt'), lines[len(lines) - 1])

    def classify(self):
        #Classifies unknown forum posts
        if self.fit == False:
            print("Fitting must be performed before classifying")
            return

        Vectorizer = vectorizer.Vectorizer(self.Dictionary.dictionary)
        input_file = input("Enter the name of the .txt file containing the unknown posts (including file-ending: ")
        try:
            with open(input_file, "r") as file:
                vectors = Vectorizer.vectorize(self.PreProcessor.PreProcess(input_file))
        except FileNotFoundError:
            if input("File not found. Press enter to try again or type 'm' and press enter to return to menu.").lower() == "m":
                return
            self.classify()
            return

        with open("result.txt", "w") as result_file:
            for line in self.Classifier.classify(vectors):
                result_file.write((label_list[line] + "\n"))
        print ("Result saved in result.txt. The predicted label of each post is printed on the corresponding line of the document.")

    def preprocess_and_fit(self):
        #Method that preprocesses data, indexes all words, vectorizes all posts and finally trains and tests the classifier
        processed = []
        processed_test = []
        for category in self.categories:
            processed.append(self.PreProcessor.PreProcess('training' + str(category) + ".txt"))
            processed_test.append(self.PreProcessor.PreProcess('testing' + str(category) + ".txt"))

        #Word indexing
        for category in processed:  # indexes all words into dictionary
            self.Dictionary.IndexWords(category)
        print("Words indexed. Dictionary size: ", len(self.Dictionary.dictionary), " words")

        #Vectorization
        Vectorizer = vectorizer.Vectorizer(self.Dictionary.dictionary)  # initializes Vectorizer-object with dictionary
        vector_start = time.time()
        print("Vectorizing...")
        training_vectors = []
        testing_vectors = []
        for category in processed:
            training_vectors.append(Vectorizer.vectorize(category))
        for category in processed_test:
            testing_vectors.append(Vectorizer.vectorize(category))
        vector_time = time.time() - vector_start
        print("Vectorization completed in ", ("%.2f" % vector_time), "seconds")

        #Training and evaluation
        self.Classifier.train(training_vectors)
        self.fit = True
        self.Classifier.evaluate(testing_vectors)

def menu():
    valid_options = ["1","2","3","4","0"]
    choice = "-1"
    while choice not in valid_options:
        choice = input("\nMenu:\n" +
          "1. Set categories\n" +
          "2. Extract\n" +
          "3. Preprocess and fit data\n"
          "4. Classify unknown posts\n"
          "0. Exit\n")
    return choice

def main():
    Hamlet = naive_bayes_classifier()
    choice = -1
    while choice != 0:
        choice = int(menu())
        if choice == 1:
            Hamlet.set_categories()
        if choice == 2:
            Hamlet.extract()
        if choice == 3:
            Hamlet.preprocess_and_fit()
        if choice == 4:
            Hamlet.classify()
        choice = -1
main()