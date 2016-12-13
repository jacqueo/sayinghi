# Prints mean, median, mode, range, variance, and standard deviation

# Initial imports and data
import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

# Sort data into pandas df
data = data.split()
data = [i.split(',') for i in data]
column_names = data[0]
data_rows = data[1:]
df = pd.DataFrame(data_rows, columns=column_names)
print(df)

# Convert to workable type, floats
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# Run stats calcuations on new df
Amean = df['Alcohol'].mean()
Amedian = df['Alcohol'].median()
Amode = stats.mode(df['Alcohol']).mode[0]
Arange = max(df['Alcohol']) - min(df['Alcohol'])
Avariance = df['Alcohol'].var()
Astandard_div = df['Alcohol'].std()

Tmean = df['Tobacco'].mean()
Tmedian = df['Tobacco'].median()
Tmode = stats.mode(df['Tobacco']).mode[0]
Trange = max(df['Tobacco']) - min(df['Tobacco'])
Tvariance = df['Tobacco'].var()
Tstandard_div = df['Tobacco'].std()

print("The mean for the Alcohol and Tobacco dataset respectively is %f and %f" % (Amean, Tmean))
print("The median for the Alcohol and Tobacco dataset respectively is %f and %f" % (Amedian, Tmedian))
print("The mode for the Alcohol and Tobacco dataset respectively is %f and %f" % (Amode, Tmode))
print("The range for the Alcohol and Tobacco dataset respectively is %f and %f" % (Arange, Trange))
print("The variance for the Alcohol and Tobacco dataset respectively is %f and %f" % (Avariance, Tvariance))
print("The standard diviation for the Alcohol and Tobacco dataset respectively is %f and %f" % (Astandard_div, Tstandard_div))



# If trying to combine column series
"""ATmean = df[['Alcohol', 'Tobacco']].mean(axis=1)
ATrange = max(max(df['Alcohol']), max(df['Tobacco'])) - min(min(df['Alcohol']), min(df['Tobacco']))
...more to work on here..."""






