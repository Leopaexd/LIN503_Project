import extractor
import preprocessor
import dictionary
import vectorizer
import dataset_divider
import classifier
import time
from multiprocessing import pool


start = time.time()
Extractor = extractor.Extractor()
PreProcessor = preprocessor.PreProcessor()
Dictionary = dictionary.Dictionary()

#lines1 = (Extractor.Extract('flashback1.json','extracted1.txt')) #extracts text from json file and stores number of lines in variable
#lines2 = (Extractor.Extract('flashback2.json','extracted2.txt'))
#lines3 = (Extractor.Extract('flashback3.json','extracted3.txt'))

#dataset_divider.Divider.Divide("extracted1.txt",lines1) #divides into training and test data
#dataset_divider.Divider.Divide("extracted2.txt",lines2)
#dataset_divider.Divider.Divide("extracted3.txt",lines3)

processed = []
processed.append(PreProcessor.PreProcess('training1.txt')) #pre-processing of training data
processed.append(PreProcessor.PreProcess('training2.txt'))
#processed.append(PreProcessor.PreProcess('training3.txt'))
#processed.append(PreProcessor.PreProcess('training4.txt')) #smaller data set for testing program
#processed.append(PreProcessor.PreProcess('training5.txt')) #smaller data set for testing program

processed_test = []
processed_test.append(PreProcessor.PreProcess('testing1.txt')) #pre-processing of testing data
processed_test.append(PreProcessor.PreProcess('testing2.txt'))
#processed_test.append(PreProcessor.PreProcess('testing3.txt'))
#processed_test.append(PreProcessor.PreProcess('testing4.txt')) #smaller data set for testing program
#processed_test.append(PreProcessor.PreProcess('testing5.txt')) #smaller data set for testing program

for category in processed: #indexes all words into dictionary
    Dictionary.IndexWords(category)
print ("Dictionary size: ", len(Dictionary.dictionary), " words")

Vectorizer = vectorizer.Vectorizer(Dictionary.dictionary) #initializes Vectorizer-object with dictionary
vector_start = time.time()
print("Vectorizing...")
training_vectors = []
testing_vectors = []
for category in processed:
     training_vectors.append(Vectorizer.vectorize(category))
for category in processed_test:
    testing_vectors.append(Vectorizer.vectorize(category))
vector_time = time.time() - vector_start
print("Vectorization completed in ",("%.2f" % vector_time), "seconds")

Classifier = classifier.Classifier(training_vectors)
Classifier.evaluate(testing_vectors)

print ("Total running time: ", ("%.2f" % (time.time()-start))," seconds")