# Outputs the frequencies, boxplot, histogram, and QQ-plot on the given data.

data = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

# Imports for frequency
import collections

# Imports for box, hist, and QQ plots
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# Frequency
c = collections.Counter(data)
print(c)

count_instances = sum(c.values())
for k, v in c.items():
	print('The frequency for ' + str(k) + ' is ' + str(v / count_instances))

# Boxplot
plt.boxplot(data)
plt.savefig("boxplot.png")

# Histogram
plt.hist(data, histtype='bar')
plt.savefig("histplot.png")

# QQ-plot
plt.figure()
graph1 = stats.probplot(data, dist='norm', plot=plt)
plt.savefig("QQ-plot.png")
