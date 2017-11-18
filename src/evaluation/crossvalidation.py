import pandas as pd
import numpy as np

def accuracy(pred, actual):
    compare = pd.DataFrame({'pred': pred, 'actual': actual})
    compare['correct'] = (compare.pred == compare.actual).apply(lambda x: int(x))
    
    crosstab = pd.crosstab(compare.pred, compare.actual, margins=True)
    accuracy = compare.correct.sum() / compare.correct.count()
    size = len(compare)
    print('size: {0:d}, accuracy: {1:.3f}'.format(size, accuracy))
    
    output = {'crosstable': crosstab, 'accuracy': accuracy, 'compare': compare}
    return output

def dfsplit(train, num, seed):
    np.random.seed(seed)
    splitdf = train.assign(splitflg = np.random.randint(0, num, len(train)))
    return splitdf







