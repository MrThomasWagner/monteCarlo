
# coding: utf-8

# In[35]:

import random
import matplotlib.pyplot as plt
import math
get_ipython().magic(u'matplotlib inline')


# In[36]:

#just reading in a file
def get_data(dataFile):
    data_IN = open(dataFile)
    return [line.strip() for line in data_IN]


# In[37]:

#trials - number of times to sum a randomnly generated list
#data - the raw data used to construct each randomnly generated list
#num_entries - the length each randomnly generated list should be

def approx_monte_carlo(trials, data, num_entries):
    results = []
    for y in range(trials):
        total = sum([int(random.choice(data)) for x in range(num_entries)])
        results.append(total)
        
    return results


# In[47]:

#fileIn - file containing the raw data
#num_entries - the length each randomnly generated list should be

def plot_it(fileIn, num_entries, trials=2000, buckets=50):
    approx = approx_monte_carlo(trials, get_data(fileIn), num_entries)
    plt.hist(approx, buckets)
    plt.title("Histogram")
    plt.xlabel("Sum of counts")
    plt.ylabel("Number of random trials of sum X")
    plt.show()


# In[48]:

CURRENT_NUM_SAMPLES = 1000
NUM_NEW_SAMPLES = 500
TOTAL_NEW_SAMPLES = NUM_NEW_SAMPLES + CURRENT_NUM_SAMPLES


# In[53]:

# Here is the main call.  Increasing the trials will generate a smoother bell curve, but will take longer. (Try 100 and 2000 to see the difference)
plot_it('set1/counts', TOTAL_NEW_SAMPLES, trials=1000)


# In[ ]:



