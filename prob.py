import collections
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(testlist)

print c

# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.iteritems():
    print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

plt.figure()
plt.boxplot(x)
plt.savefig("boxplot.png")

plt.figure()
# How to get all the labels for histogram?
plt.hist(x, histtype="bar", bins=range(1,11), align="left")
plt.savefig("hist.png")

plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("normal_qq.png")

plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.savefig("uniform_qq.png")


