# Chisquare Test
# Load data, clean data, perform chisquare test, and print.

# all imports
import pandas as pd
import collections
from scipy import stats
import matplotlib.pyplot as plt

# load data
loanData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# clean data
loanData.dropna(inplace=True)

# set up chisquare test variables
freq = collections.Counter(loanData['Open.CREDIT.Lines'])

# will need observed and expected values for chi-test
# using freq.values() as our observed; expected is assumed normal distribution.

# run chisquared test
chi, p = stats.chisquare(list(freq.values())) # add 'list' in python3 to turn 'dict_values' into list.

# print results
print('chisquare is %f' %chi) 
print('p-value is %f' %p)

# show plot
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()
