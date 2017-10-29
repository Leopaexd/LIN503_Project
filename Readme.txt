### TABLE OF CONTENTS ###
Introduction
Requirements
Modules
How to use (demonstration mode, using Hamlet.py)
How to use Scraper

######################################## Introduction ####################################################
This project consists of several tools created to enable classification of Swedish forum posts into different categories using a Naive Bayes classifier. It's intended use is as a part of data-mining and analysis; it is not very useful by itself, other than as a proof of concept.


*WARNING* Many of the .json and .txt-files used by this project will be very large, so make sure you use a text editor that supports large files (such as notepad++). Using Windows notepad to open these files is not recommended. 

######################################## Requirements ####################################################
This project was developed using Python 3.6. It may run on other 3.X versions, but this has not been tested.

The following modules/packages are required to use the project (note that Scikit-learn requires NumPy and SciPy):

Scrapy (Only if you intend to use Scraper to do the scraping yourself) https://doc.scrapy.org/en/latest/intro/install.html
NLTK (http://www.nltk.org/install.html)
NumPy+MKL (https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)
SciPy (https://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy)
Scikit-learn (http://scikit-learn.org/stable/install.html) (requires NumPy and SciPy)

The project has only been tested using the following versions of above packages (other versions may work):
Scrapy - 1.4
NLTK - 3.2.5
NumPy+MKL - 1.13.3+mkl
SciPy - 0.19.1
Scikit-learn - 0.19.1

################################ Modules (in expected order of use) ######################################
Scraper - an implementation of a Scrapy spider designed to extract posts from the Swedish forum flashback.org. Output is generated in the form of .json-files containing forum posts.

Extractor - extracts text from the .json-files created by Scraper and removes interpunctuation. Generates output in the form of .txt-files with one post per line.

Preprocessor - preprocesses the posts by removing stop words, tokenizing the remaining words to a list of strings and stemming all words.

Dictionary - used to index all words in the training data to a dict-object, with the string as key and its index as value.

Dataset_divider - divides the training data into training and testing data (to give an estimate of classifier performance). 90 percent of the data is used to train the classifier, 10 percent to test it.

Vectorizer - generates a feature vector for each post. The feature vector contains the relative frequency of all recognized words (those that are found in the dictionary) at their respective indices (according to the dictionary). The vectors are represented by one-dimensional sparse matrices
(using csr_matrix from Scipy).

Classifier - this module handles the actual classification. It uses Multinomial Naive Bayes from sklearn.

Hamlet - a simple command line user interface to demonstrate the project

testfile - module used for testing the project during development.

######################## How to use (demonstration mode, using Hamlet.py) ##############################
1. Make sure you have extracted the json-files flashback1.json-flashback7.json in the working folder. Either from the json-files.zip archive (password required due to copyright concerns) or by using the Scraper (requires minor editing of Scraper.py and use of Scrapy). To unzip, use 7zip or similar software that supports archives encrypted with AES-256. If you wish to run Scraper yourself, instructions can be found in the next section of the readme.

2. Run Hamlet.py and select categories to use 

3. Select "2. Extract data from json-files". This extracts data to .txt-files in your working folder. This step does not have to be repeated if running the program multiple times, provided the selected categories have been extracted at least once.

4. Select "3. Preprocess and fit data". This step involves converting all posts to feature vectors, running time varies depending on amount of data (categories chosen). Expect 5-8 minutes depending on computer and categories. The program will report time taken when it finishes.

5. You can now use the classifier to classify a list of unknown forum posts. The posts should be listed in a .txt-file with one post per line (no linebreaks in the posts themselves) placed in the working folder, all interpunctuation should also be removed. Preprocessing will be performed before classification, so there is no need to remove stop words or stem the word (but it won't cause any problems if you do). To try this feature, it is recommended that you copy and paste lines trainingX.txt-files for different categories (where X is the category number). 

Output will be written line by line to result.txt in the working folder, each line will state the label (name) of the category of the corresponding post. Viewing the files in a text editor that shows line numbers is therefore recommended.

############################### How to use Scraper ######################################
1. Make sure you have Scrapy installed (https://doc.scrapy.org/en/latest/intro/install.html)
2. Edit Scraper.py and make sure only one line in method 'start_requests' is uncommented. If more than one category is uncommented, the categories will not be kept separate and the classifier will not work as intended.
3. Using a terminal, open your working folder and execute the command 'scrapy runspider Scrapy.py -o flashbackX.json' where X is the number of the chosen category (as indicated by the comment on the same line in Scraper.py). This will scrape all posts on that subforum and save them in a json-file, ready to be extracted using the extractor.py module or Hamlet.py.

