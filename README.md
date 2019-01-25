# Decision Tree Constraints 

This is a sample code of the `PruneToSizeK` method for sklearn [Decision Tree Classifier](https://scikit-learn.org/stable/modules/tree.html).

Install:
```
pip install DecisionTreeConstraints
```

Usage:
```
from sklearn.datasets import load_iris
from sklearn import tree
from DecisionTreeConstraints import SizeConstraintPruning

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

MAX_SIZE=6
SizeConstraintPruning(MAX_SIZE).pruneToSizeK(clf)

accuracy = clf.score(iris.data, iris.target)
print('Training accuracy for max size %s: %.3f' % (MAX_SIZE, accuracy))
```

Garofalakis, M., Hyun, D., Rastogi, R. et al. Data Mining and Knowledge Discovery (2003) 7: 187. [doi:10.1023](https://doi.org/10.1023/A:1022445500761).
