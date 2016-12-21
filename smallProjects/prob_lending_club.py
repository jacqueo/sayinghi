# Reads and Cleans Lending Club data and creates 3 graphs on 'Amount.Requested' to compare against "Amount.Funded.By.Investors"

# Inital imports
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Read data
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# Clean data
loansData.dropna(inplace=True)

# Generate plots (box, hist, QQ)
#Box
loansData.boxplot(column='Amount.Requested')
plt.savefig('loansBox.png')


#Hist
loansData.hist('Amount.Requested', histtype='bar')
plt.savefig('loansHist.png')

#QQ plot
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist='norm' ,plot=plt)
plt.savefig('loansQQ.png')

# Notes and comparisons on plots
print('On Boxplot, the two graphs are nearly identical.')
print('On Histograms, there is less peak height differentiation within "Amounts.Requested"')
print('On QQ-plots, neither is a good example of normal distributed data, R-scores are 0.93 and 0.928 respectively.')
