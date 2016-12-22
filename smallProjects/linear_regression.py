# Linear Regression and Correlation
# Goal: Clean and Plot Data to show Linear Regression Graphs

import pandas as pd
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# first 5 rows of data, see what we're working with.
loansData['Interest.Rates'][0:5]
loansData['Loan.Length'][0:5]
loansData['FICO.Range'][0:5]

# clean data and replace into loansData DataFrame
loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]
loansData['Loan.Length'] = [int(elm.replace('months','')) for elm in loansData['Loan.Length']]
loansData['FICO.Score'] = [int(elm.split('-')[0]) for elm in loansData['FICO.Range']]

# view updated DataFrame with new columns (1) Interest.Rate (2) Loan.Length (3) FICO.Score
print(loansData) 

# Ploting with Cleaned Data 
import matplotlib.pyplot as plt


#Histogram of FICO Score
plt.figure()
plt.hist(loansData['FICO.Score'])
plt.savefig('FICOhist.png') 

#Scatter Plot of all loansData
plt.figure()
p = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.savefig('loansDataScatterPlot.png') 

# Linear Regression Analysis
# linear model will look something like this: InterestRate = b + a1(FICOScore) + a2(LoanAmount)

# everything you need going forward
import numpy as np
import pandas as pd
import statsmodels.api as sm

# extracted columns for our equation:
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# creating our variables

# the dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# put 2 columbs together to cerate an "input matrix"
x = np.column_stack([x1,x2])

# now we create a linear model:
X = sm.add_constant(x)
model = sm.OLS(y, X)
f = model.fit()

# view results summary:
f.summary()

