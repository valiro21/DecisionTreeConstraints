from math import log2, pi
from scipy.special import gamma
import numpy as np

def costOfData(tree, index):
    numberOfRecords = tree.value[index].sum()
    numberOfClasses = np.count_nonzero(tree.value[index][0])
    
    total = (numberOfClasses - 1) / 2 * log2(numberOfRecords / 2)
    total += log2(pow(pi, numberOfClasses / 2) / gamma(numberOfClasses / 2))
    for numberOfClassRecords in tree.value[index][0]:
        if numberOfClassRecords == 0:
            continue
        
        total += numberOfClassRecords * log2(numberOfRecords / numberOfClassRecords)                        
        
    return total


def costOfSplitNode(tree, index):
    feature = tree.feature[index]
    thresholdCount = len(tree.threshold[tree.feature == feature])
    
    return log2(tree.n_features - 1) + log2(thresholdCount)
