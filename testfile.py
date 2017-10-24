import extractor
import preprocessor
import dictionary
import vectorizer


#Extractor = extractor.Extractor()
PreProcessor = preprocessor.PreProcessor()
Dictionary = dictionary.Dictionary()


#Extractor.Extract('flashback1.json','extracted1.txt')
#Extractor.Extract('flashback2.json','extracted2.txt')
#Extractor.Extract('flashback3.json','extracted3.txt')

processed = []
processed.append(PreProcessor.PreProcess('extracted1.txt'))
#processed.append(PreProcessor.PreProcess('extracted2.txt'))
#processed.append(PreProcessor.PreProcess('extracted3.txt'))

for category in processed:
    Dictionary.IndexWords(category)

Vectorizer = vectorizer.Vectorizer(Dictionary.dictionary)

vectors = []

for category in processed:
    vectors.append([Vectorizer.vectorize(post)for post in category])
print("Finished")

for number in vectors[0][2]:
    if number != 0:
        print(number)
