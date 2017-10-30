from extractor import Extractor
import preprocessor
import dictionary
import vectorizer
import dataset_divider
import classifier
import time

start = time.time()
PreProcessor = preprocessor.Preprocessor()
Dictionary = dictionary.Dictionary()
categories = [1, 2, 3]  # Categories to be includes

lines = []
for category in categories:
    lines.append(Extractor.extract(('flashback' + str(category) + '.json'), ('extracted' + str(category) + '.txt')))
    dataset_divider.Divider.divide(('extracted' + str(category) + '.txt'), lines[len(lines) - 1])

# pre-processing of training data
processed = []
processed_test = []
for category in categories:
    processed.append(PreProcessor.preprocess('training' + str(category) + ".txt"))
    processed_test.append(PreProcessor.preprocess('testing' + str(category) + ".txt"))

with open("testingposts.txt", "w") as file:
    poststring = ""
    counter = 0
    for category in processed_test:
        for post in category:
            counter += 1
            for word in post:
                poststring += (word + " ")
            file.write(poststring)
            poststring = "\n"

for category in processed:  # indexes all words into dictionary
    Dictionary.index_words(category)
print("Words indexed. Dictionary size: ", len(Dictionary.dictionary), " words")

with open("dictionary.txt", "w") as file:
    for key in Dictionary.dictionary.keys():
        file.write((key + "\n"))

Vectorizer = vectorizer.Vectorizer(Dictionary.dictionary)  # initializes Vectorizer-object with dictionary
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

Classifier = classifier.Classifier()  # instantiates Classifier and fits training data
Classifier.train(training_vectors)
Classifier.evaluate(testing_vectors)

label_list = ["Candy", "Physics, math and technology", "Nazism", "Pets", "Roleplaying and board games",
              "Relationship advice", "Cannabis"]
result_file = open("result.txt", "w")
for line in Classifier.classify(testing_vectors):
    result_file.write((label_list[line] + "\n"))
result_file.close()

with open("incorrectposts.txt", "w") as file:
    poststring = ""
    counter = 0
    for category in processed_test:
        for post in category:
            counter += 1
            if counter in Classifier.incorrect_list:
                for word in post:
                    poststring += (word + " ")
                file.write(poststring)
                poststring = "\n"

print("Total running time: ", ("%.2f" % (time.time() - start)), " seconds")
