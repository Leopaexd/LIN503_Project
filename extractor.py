# Author: Oliver Glant
# Class for extracting swedish forum posts from json-file created by scraper, also returns number of lines

import re
import time


class Extractor(object):
    @staticmethod
    def extract(input_file, output_file):
        # extract text line by line from json file to txt, remove non-alphanumeric characters and enforce lower case
        output = open(output_file, 'w')
        with open(input_file) as file:
            text_file = file.readlines()
        start = time.time()
        print("Extracting " + input_file)
        count = 0
        for line in text_file:
            count += 1
            text = line.strip('{"post": [').replace('\\u00e5', 'å').replace('\\u00e4', 'ä').replace('\\u00f6', 'ö')
            text = text.replace('\\u00c5', 'Å').replace('\\u00c4', 'Ä').replace('\\u00d6', 'Ö').replace('\\u00e9', 'é')
            text = text.replace('\\n', '').replace('\\r', '').replace('\\t', '').replace('"', '').replace(']},', '')
            text = text.replace('.', ' ').replace(',', '').replace('!', '').replace('?', '').replace('\\', '')
            text = text.replace('(', '').replace(')', '').replace('-', '').replace('=', '').replace(':', '')
            text = text.replace('/', ' ')  # for alternatives denoted by slashes
            text = text.lower()
            text = re.sub('[^A-Öa-ö] ', ' ', text)
    #       text = re.sub('\)\(', ' ', text)
            output.write(text)
        output.close()
        time_elapsed = time.time() - start
        print("Extraction completed in ", ("%.2f" % time_elapsed), "seconds")
        return count
