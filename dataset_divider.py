# Author: Oliver Glant
# Divides dataset into training and testing parts at ratio 9:1


class Divider(object):

    @staticmethod
    def divide(datafile, lines):
        label = datafile.strip(".txt")[-1:]
        file = open(datafile, "r")
        training = open(('training' + str(label) + ".txt"), "w")
        for _ in range(int(lines*0.9)):  # Writes first 70% of lines into trainingX.txt
            training.write(file.readline())
        testing = open(('testing' + str(label) + ".txt"), "w")
        for line in file:
            testing.write(line)
