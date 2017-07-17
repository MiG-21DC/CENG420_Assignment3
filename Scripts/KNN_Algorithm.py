import csv
from random import randint
import math
import operator


class knn:
    def __init__(self, dataset):
        self.dataset = dataset
        self.setosa = []
        self.trainset = []
        self.trainseq = []
        self.testset = []
        self.testseq = []

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

    def getTestSet(self, num=5):
        set_size = len(self.setosa)
        sequence = []
        test_data = []
        if set_size == 0 or set_size < num:
            return 'Setosa set defined error. Reload the program and try again.'
        for i in range(num):
            randnum = randint(0, set_size - 1)
            while randnum in sequence or randnum in self.trainseq:
                randnum = randint(0, set_size - 1)
            sequence.append(randnum)
        self.testseq = sequence
        for value in sequence:
            test_data.append(self.setosa[value])
        self.testset = test_data
        return test_data

    def euclideanDistance(self, instance1, instance2, length = 4):
        distance = 0
        for x in range(length):
            distance += pow((float(instance1[x]) - float(instance2[x])), 2)
        return math.sqrt(distance)

    def getNeighbors(self, trainingSet, testInstance, k=1):
        distances = []
        for x in range(len(trainingSet)):
            dist = self.euclideanDistance(testInstance, trainingSet[x])
            distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(k):
            neighbors.append(distances[x])
        return neighbors