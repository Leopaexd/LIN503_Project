# Author: Oliver Glant
# Class for extracting swedish forum posts from json-file created by scraper


import re

class Extractor(object):

    def Extract(self,file):
        #Extract flashback forum text line by line from json file to txt, remove non-alphanumeric characters and
        # enforce lower case
        output = open('extracted.txt','w')
        with open(file) as textfilen:
            textfile = textfilen.readlines()
        print("Extraction started")
        for line in textfile:
            text = line.strip('{"post": [').replace('\\u00e5','å').replace('\\u00e4', 'ä').replace('\\u00f6','ö')
            text = text.replace('\\u00c5','Å').replace('\\u00c4','Ä').replace('\\u00d6','Ö').replace('\\u00e9','é')
            text = text.replace('\\n', '').replace('\\r', '').replace('\\t', '').replace('"','').replace(']},','')
            text = text.replace('.', ' ').replace(',', '').replace('!', '').replace('?', '').replace('\\', '').replace(':', '')
            text = text.replace('(', '').replace(')', '').replace('-', '').replace('=', '')
            text = text.replace('/', ' ') #for alternatives denoted by slashes
            text = text.lower()
            text = re.sub('[^A-Öa-ö] ', ' ',text )
    #       text = re.sub('\)\(', ' ', text)
            output.write(text)
        output.close()
        print("Extraction completed")