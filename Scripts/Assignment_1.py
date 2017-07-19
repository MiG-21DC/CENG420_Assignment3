from KNN_Algorithm import knn
import sys

def main():
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
        print 'The closet neighbor of %s is:' % str(item)
        print neighbors[0][0], 'with a distance of ', neighbors[0][1]
        print 'The type of test data %s is:' % str(item), neighbors[0][0][-1], '\n'

    print 'Max distance:', A.max_dist
    print '************************************************************************', '\n'
    print 'Step 2:'
    print 'Random picked 5 setosa test set for step 2(not included in the set in step 1):'
    test2set = A.getTestSet()
    print test2set, '\n'

    for item in test2set:
        neighbors = A.getNeighbors(train_set, item, 'P2')
        if neighbors[0][1] > A.max_dist:
            iris_type = 'Versicolor'
        else:
            iris_type = 'Setosa'
        print 'The closet neighbor of %s is:' % str(item)
        print neighbors[0][0], 'with a distance of ', neighbors[0][1]
        print 'The type of test data %s is:' % str(item), iris_type, '\n'
    versicolor = A.versicolorSet()
    ver_test_set = A.getVersicolorTestSet()
    print '\nRandom picked 5 versicolor test set'
    print ver_test_set, '\n'
    for item in ver_test_set:
        neighbors = A.getNeighbors(train_set, item, 'P2')
        if float(neighbors[0][1]) > float(A.max_dist):
            iris_type = 'Versicolor'
        else:
            iris_type = 'Setosa'
        print 'The closet neighbor of %s is:' % str(item)
        print neighbors[0][0], 'with a distance of ', neighbors[0][1]
        print 'The type of test data %s is:' % str(item), iris_type, '\n'


if __name__=="__main__":
    main()