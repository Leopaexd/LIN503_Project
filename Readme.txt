################################## Introduction ####################################################
This project consists of several tools created to enable classification of Swedish forum posts into different categories.
It's intended use is as a part of data-mining and analysis; it is not very useful by itself, other than as a proof of concept.

################################ Modules (in expected order of use) ######################################

Scraper - an implementation of a Scrapy (https://doc.scrapy.org/en/latest/intro/overview.html) spider designed to extract posts from the Swedish forum flashback.org. Output is generated in the form of .json-files containing forum posts.

Extractor - extracts text from the .json-files created by Scraper and removes interpunctuation. Generates output in the form of .txt-files with one post per line.

Preprocessor - preprocesses the posts by removing stop words, tokenizing the remaining words to a list of strings and stemming all words.

Dictionary - used to index all words in the training data to a dict-object, with the string as key and its index as value.

Dataset_divider - divides the training data into training and testing data (to give an estimate of classifier performance). 90 percent of the data is used to train the classifier, 10 percent to test it.

Vectorizer - generates a feature vector for each post. The feature vector contains the relative frequency of all recognized words (those that are found in the dictionary) at their respective indices (according to the dictionary). The vectors are represented by one-dimensional sparse matrices
(using csr_matrix from Scipy).

Classifier - this module handles the actual classification. It uses Multinomial Naive Bayes from sklearn.

Hamlet - a simple command line user interface to demonstrate the project

testfile - module used for testing the project during development.

#####################################################################################################
