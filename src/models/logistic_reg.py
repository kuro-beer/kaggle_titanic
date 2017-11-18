# base setting
import sys
sys.path.append('./src/')

# libraries
from logging import StreamHandler, DEBUG, Formatter, FileHandler, getLogger
import pandas as pd
from sklearn.linear_model import LogisticRegression as lreg
from process import texthandling as th

# logger setting
logger = getLogger(__name__)
logdir = './src/models/log/'
if __name__ == '__main__':
    log_fmt = Formatter('%(asctime)s %(name)s %(lineno)d [%(levelname)s][%(funcName)s] %(message)s')
    handler = StreamHandler()
    handler.setLevel('INFO')
    handler.setFormatter(log_fmt)
    logger.addHandler(handler)

    handler = FileHandler(logdir + 'logistic_reg.py.log', 'a')
    handler.setLevel(DEBUG)
    handler.setFormatter(log_fmt)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)

# data input
logger.info('start: data input')
datadir = './input/'
train = pd.read_csv(datadir + 'train.csv')
logger.info('end: data input')

# processing
# get dummy variables
logger.info('start: data preparation')
dum_sex = pd.get_dummies(train['Sex'])
dum_emb = pd.get_dummies(train['Embarked'])

train_proc = pd.concat((train, dum_sex, dum_emb), axis = 1)
train_proc = train_proc.drop('Sex', axis = 1)
train_proc = train_proc.drop('Embarked', axis = 1)
train_proc = train_proc.drop('female', axis = 1)
train_proc = train_proc.drop('S', axis = 1)

name_df = th.FlagWords(train_proc['Name'], ['Mr', 'Master', 'Mrs', 'Miss', ])
train_proc = pd.concat([train_proc, name_df], axis=1)
train_proc = train_proc.drop('Name', axis=1)

logger.info('end: data preparation')

# logistic regression
train_proc




















