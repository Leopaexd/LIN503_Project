import extractor
import preprocessor
import dictionary
import vectorizer
import time

Extractor = extractor.Extractor()
PreProcessor = preprocessor.PreProcessor()
Dictionary = dictionary.Dictionary()


Extractor.Extract('flashback1.json','extracted1.txt')
#Extractor.Extract('flashback2.json','extracted2.txt')
#Extractor.Extract('flashback3.json','extracted3.txt')

processed = []
processed.append(PreProcessor.PreProcess('extracted1.txt'))
#processed.append(PreProcessor.PreProcess('extracted2.txt'))
#processed.append(PreProcessor.PreProcess('extracted3.txt'))

for category in processed:
    Dictionary.IndexWords(category)

Vectorizer = vectorizer.Vectorizer(Dictionary.dictionary)
vector_start = time.time()
print("Vectorizing")
vectors = []
for category in processed:
     vectors.append([Vectorizer.vectorize(post)for post in category])
vector_time = time.time() - vector_start
print("Vectorization completed in ",("%.2f" % vector_time), "seconds")
#for number in vectors[0][2]:
#    if number != 0:
#       print(number)

print ("Dictionary size: ", len(Dictionary.dictionary), " words")