from KNN_Algorithm import knn
import sys

if __name__=="__main__":
    A = knn('iris.csv')
    neighbors = []
    setosa = A.setosaSet()
    train_set = A.getTrainSet()
    test_set = A.getTestSet()
    print 'Assignment 1 \nStep 1:\nRandom picked setosa train set:'
    print train_set, '\n'
    print 'Random picked setosa test set:'
    print test_set, '\n'

    for item in test_set:
        neighbors = A.getNeighbors(train_set, item)
        print 'The closet neighbor of %s is:'%str(item)
        print neighbors[0][0], 'with a distance of ', neighbors[0][1]
        print 'The type of test data %s is:' %str(item), neighbors[0][0][-1], '\n'

    print '************************************************************************', '\n'
    print 'Step 2:'
    print 
