import numpy as np
import pandas as pd
import random
from matplotlib import pyplot as plt




train_set_file = '../data/hw1_train.csv'

train_set = pd.read_csv(train_set_file)


test_set_file = '../data/hw1_test.csv'

test_set = pd.read_csv(test_set_file)



X = train_set.iloc[:,1:]
Y = train_set.iloc[:,0]

X_test = test_set.iloc[:, 1:]
Y_test = test_set.iloc[:, 0]


sample_num = 100

class_0_indices_all = [i for i in range(Y.size) if Y.iloc[i] == -1] # class_0 for target -1
class_1_indices_all = [i for i in range(Y.size) if Y.iloc[i] == 1] # class_1 for target 1


# Selecting random samples

class_0_index_samp = random.sample(class_0_indices_all, sample_num)
class_1_index_samp = random.sample(class_1_indices_all, sample_num)



for i in class_0_index_samp:
    plt.plot(range(500), X.iloc[i], 'r')
    
for i in class_1_index_samp:
    plt.plot(range(500), X.iloc[i], 'b')

plt.savefig('../latex/figs/plot.png')



