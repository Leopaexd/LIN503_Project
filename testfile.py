import extractor
import preprocessor


Extractor = extractor.Extractor()
PreProcessor = preprocessor.PreProcessor()

extracted = Extractor.Extract('flashback.json')
processed = PreProcessor.preprocess('extracted.txt')
print("Finished")
#print(processed)