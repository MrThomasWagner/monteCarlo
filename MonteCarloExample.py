
# coding: utf-8

# In[3]:

import random
import matplotlib.pyplot as plt
import math
get_ipython().magic(u'matplotlib inline')


# In[4]:

def get_data(dataFile):
    data_IN = open(dataFile)
    return [line.strip() for line in data_IN]


# In[5]:

def approx_monte_carlo(trials, data, numSites):
    results = []
    for y in range(trials):
        total = sum([int(random.choice(data)) for x in range(numSites)])
        results.append(total)
        
    return results


# In[6]:

def main(fileIn, numSamples, trials=2000, buckets=50):
    approx = approx_monte_carlo(trials, get_data(fileIn), numSamples)
    plt.hist(approx, buckets)
    plt.title(fileIn)
    plt.show()


# In[7]:

CURRENT_NUM_SAMPLES = 1000
NUM_NEW_SAMPLES = 500
TOTAL_NEW_SAMPLES = NUM_NEW_SAMPLES + CURRENT_NUM_SAMPLES


# In[8]:

main('set1/counts', TOTAL_NEW_SAMPLES, trials=1000)


# In[9]:

main('set2/counts', TOTAL_NEW_SAMPLES, trials=1000)


# In[ ]:



