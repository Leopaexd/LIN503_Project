import extractor
import preprocessor
import dictionary
import vectorizer
import dataset_divider
import classifier
import time

start = time.time()
Extractor = extractor.Extractor()
PreProcessor = preprocessor.PreProcessor()
Dictionary = dictionary.Dictionary()

lines1 = (Extractor.Extract('flashback1.json','extracted1.txt')) #extracts text from json file and stores number of lines in variable
lines2 = (Extractor.Extract('flashback2.json','extracted2.txt'))
lines3 = (Extractor.Extract('flashback3.json','extracted3.txt'))
lines4 = (Extractor.Extract('flashback4.json','extracted4.txt'))
lines5 = (Extractor.Extract('flashback5.json','extracted5.txt'))
lines6 = (Extractor.Extract('flashback6.json','extracted6.txt'))

dataset_divider.Divider.Divide("extracted1.txt",lines1) #divides into training and test data
dataset_divider.Divider.Divide("extracted2.txt",lines2)
dataset_divider.Divider.Divide("extracted3.txt",lines3)
dataset_divider.Divider.Divide("extracted4.txt",lines4)
dataset_divider.Divider.Divide("extracted5.txt",lines5)
dataset_divider.Divider.Divide("extracted6.txt",lines6)

#pre-processing of training data
processed = []
processed.append(PreProcessor.PreProcess('training1.txt'))
processed.append(PreProcessor.PreProcess('training2.txt'))
processed.append(PreProcessor.PreProcess('training3.txt')) #nazism
processed.append(PreProcessor.PreProcess('training4.txt')) #pets
#processed.append(PreProcessor.PreProcess('training5.txt'))
processed.append(PreProcessor.PreProcess('training6.txt'))

processed_test = []
processed_test.append(PreProcessor.PreProcess('testing1.txt')) #pre-processing of testing data
processed_test.append(PreProcessor.PreProcess('testing2.txt'))
processed_test.append(PreProcessor.PreProcess('testing3.txt'))
processed_test.append(PreProcessor.PreProcess('testing4.txt')) #pets
#processed_test.append(PreProcessor.PreProcess('testing5.txt'))
processed_test.append(PreProcessor.PreProcess('testing6.txt'))
#processed_test.append(PreProcessor.PreProcess('trial1.txt'))
#processed_test.append(PreProcessor.PreProcess('trial2.txt'))

for category in processed: #indexes all words into dictionary
    Dictionary.IndexWords(category)
print ("Dictionary size: ", len(Dictionary.dictionary), " words")

with open("dictionary.txt", "w") as file:
    for key in Dictionary.dictionary.keys():
        file.write((key + "\n"))

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

Classifier = classifier.Classifier(training_vectors) #instantiates Classifier and fits training data
Classifier.evaluate(testing_vectors)

label_list = ["Candy","Physics, math and technology","Nazism","Pets","Roleplaying and board games","Relationship advice"]
result_file = open("result.txt","w")
for line in Classifier.classify(testing_vectors):
    result_file.write((label_list[line] + "\n"))
result_file.close()


print ("Total running time: ", ("%.2f" % (time.time()-start))," seconds")