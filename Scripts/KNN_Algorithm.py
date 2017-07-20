import csv
from random import randint
import math
import operator


class knn:
    def __init__(self, dataset='iris.csv'):
        self.dataset = dataset
        self.setosa = []
        self.trainset = []
        self.trainseq = []
        self.testset = []
        self.testseq = []
        self.max_dist = 0
        self.test2set = []
        self.test2seq = []
        self.versicolor = []
        self.vertestseq = []
        self.vertestset = []

    # Load all setosa set from iris csv file
    def setosaSet(self):
        with open(self.dataset,'rb') as csvfile:
            line = csvfile.readline()
            while line != '':
                line.replace('\n', '')
                elements = line.split(',')
                elements[4] = elements[4].split('\r\n')[0]
                if elements[4] == 'Iris-setosa':
                    self.setosa.append(elements)
                line = csvfile.readline()

        return self.setosa

    # Load all versicolor set from iris csv file
    def versicolorSet(self):
        with open(self.dataset,'rb') as csvfile:
            line = csvfile.readline()
            while line != '':
                line.replace('\n', '')
                elements = line.split(',')
                elements[4] = elements[4].split('\r\n')[0]
                if elements[4] == 'Iris-versicolor':
                    self.versicolor.append(elements)
                line = csvfile.readline()
        return self.versicolor

    # Random pick 10 setosa set for training
    def getTrainSet(self, num=10):
        set_size = len(self.setosa)
        sequence = []
        train_data = []
        if set_size == 0 or set_size < num:
            return 'Setosa set defined error. Reload the program and try again.'
        for i in range(num):
            randnum = randint(0, set_size - 1)
            while randnum in sequence:
                randnum = randint(0, set_size - 1)
            sequence.append(randnum)
        self.trainseq = sequence
        for value in sequence:
            train_data.append(self.setosa[value])
        self.trainset = train_data
        return train_data

    # Random pick 5 setosa set for testing for both step 1 and 2.
    def getTestSet(self, num=5, key='setosa'):
        if key == 'setosa':
            dataset = self.setosa
        set_size = len(dataset)
        sequence = []
        test_data = []
        if set_size == 0 or set_size < num:
            return 'Setosa set defined error. Reload the program and try again.'
        for i in range(num):
            randnum = randint(0, set_size - 1)
            while randnum in sequence or randnum in self.trainseq or randnum in self.testseq:
                randnum = randint(0, set_size - 1)
            sequence.append(randnum)
        if self.testseq == []:
            self.testseq = sequence
            for value in sequence:
                test_data.append(dataset[value])
            self.testset = test_data
        else:
            self.test2seq = sequence
            for value in sequence:
                test_data.append(dataset[value])
            self.test2set = test_data

        return test_data

    # Random pick 5 versicolor set for testing for step 2
    def getVersicolorTestSet(self, num=5):
        dataset = self.versicolor
        set_size = len(dataset)
        sequence = []
        test_data = []
        if set_size == 0 or set_size < num:
            return 'Setosa set defined error. Reload the program and try again.'
        for i in range(num):
            randnum = randint(0, set_size - 1)
            while randnum in sequence:
                randnum = randint(0, set_size - 1)
            sequence.append(randnum)
        if self.vertestseq == []:
            self.vertestseq = sequence
            for value in sequence:
                test_data.append(dataset[value])
            self.vertestset = test_data
        else:
            print 'Load versicolor error. Rerun the program and try again'
            return 0

        return test_data

    # Calculate distance between two sets
    def euclideanDistance(self, instance1, instance2, length = 4):
        distance = 0
        for x in range(length):
            distance += pow((float(instance1[x]) - float(instance2[x])), 2)
        return math.sqrt(distance)

    # Judge the closet neighbor between test set and training set
    def getNeighbors(self, trainingSet, testInstance, q='P1',k=1):
        distances = []
        for x in range(len(trainingSet)):
            print testInstance
            print trainingSet[x]
            dist = self.euclideanDistance(testInstance, trainingSet[x])
            distances.append((trainingSet[x], dist))
            if q == 'P1':
                if dist > self.max_dist:
                    self.max_dist = dist
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(k):
            neighbors.append(distances[x])
        return neighbors

