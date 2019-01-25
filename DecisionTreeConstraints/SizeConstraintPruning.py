from sklearn.tree._tree import TREE_LEAF
from DecisionTreeConstraints.MDL import costOfData, costOfSplitNode

def isLeaf(tree, index):
    return tree.children_left[index] == TREE_LEAF and tree.children_right[index] == TREE_LEAF

class SizeConstraintPruning():
    def __init__(self, size=3, verbose=False):
        self.cost = {}
        self.size = size
        self.verbose = verbose
        
    def get(self, tree, index, size, depth):
        if index not in self.cost:
            self.cost[index] = {}
        
        if size not in self.cost[index]:
            self.cost[index][size] = {
                'cost': float('inf'),
                'sizeLeft': 0
            }
            
            self.computeCost(tree, index, size, depth)
            
        return self.cost[index][size]
        
    def computeCost(self, tree, index, size, depth):
        if self.verbose:
            print("".join(['-'] * depth), 'Computing cost for index', index, 'and size', size)
            
        self.cost[index][size]['cost'] = costOfData(tree, index) + 1
        if size >= 3 and not isLeaf(tree, index):
            self.cost[index][size]['cost'] = costOfData(tree, index) + 1
            for sizeLeft in range(1, size-1):
                sizeRight = size - sizeLeft - 1
                
                indexLeft = tree.children_left[index]
                costLeft = self.get(tree, indexLeft, sizeLeft, depth + 1)['cost']
                
                indexRight = tree.children_right[index]
                costRight = self.get(tree, indexRight, sizeRight, depth + 1)['cost']

                nodeCost = 1 + costOfSplitNode(tree, index) + costLeft + costRight

                if nodeCost < self.cost[index][size]['cost']:
                    self.cost[index][size]['cost'] = nodeCost
                    self.cost[index][size]['sizeLeft'] = sizeLeft
        
        if self.verbose:
            print("".join(['-'] * depth), self.cost[index][size])
    
    
    def _pruneToSizeK(self, tree, index, size, depth):
        if self.verbose:
            print("".join(['-'] * depth), 'Pruning index', index, 'to size', size)
            
        if isLeaf(tree, index):
            return
        
        cost = self.get(tree, index, size, depth)
        if size < 3 or cost['sizeLeft'] == 0:
            tree.children_left[index] = TREE_LEAF
            tree.children_right[index] = TREE_LEAF        
        else:
            sizeLeft = cost['sizeLeft']
            sizeRight = size - sizeLeft - 1

            self._pruneToSizeK(tree, tree.children_left[index], sizeLeft, depth + 1)
            self._pruneToSizeK(tree, tree.children_right[index], sizeRight, depth + 1)

        
    def pruneToSizeK(self, tree, verbose=False):
        self._pruneToSizeK(tree.tree_, 0, self.size, 0)
