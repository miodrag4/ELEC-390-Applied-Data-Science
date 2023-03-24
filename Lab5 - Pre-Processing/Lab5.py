import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_set = pd.read_csv('Lab 5/unclean-wine-quality.csv')

# Question 1
#drop first column
data_set = data_set.drop(data_set.columns[0], axis=1)

labels = data_set.iloc[:,11]
data = data_set.iloc[:,0:11]

# use np.where to and sum to count number of - and NaN values
print('\nQuestion 1: \n')
print('number of - values: ', np.sum(np.where(data == '-', 1, 0)))
print ('Number of NaN values: ', np.sum(np.where(data.isnull(), 1, 0)))

# Print the indicies of the - values in the dataset
print('Indicies of - values: \n', np.where(data == '-'))
print ('Indicies of NaN values: \n', np.where(data.isnull()))

# Change all - values to NaN
print('\nReplacing all - values with NaN')
data = data.replace('-', np.nan)

# Print number of null values in the dataset
print ('Number of NaN values: ', np.sum(np.where(data.isnull(), 1, 0)))

# Change all values in the data set to float64
data = data.astype('float64')

# Question 2
# Filling missing values with a constant value
print ('\nQuestion 2: \n')
data2 = data
data2 = data2.fillna({'fixed acidity': 0})
data2 = data2.fillna({'volatile acidity': 0})
data2 = data2.fillna({'citric acid': 0})
data2 = data2.fillna({'residual sugar': 0})
data2 = data2.fillna({'chlorides': 1})
data2 = data2.fillna({'free sulfur dioxide': 0})
data2 = data2.fillna({'total sulfur dioxide': 0})
data2 = data2.fillna({'density': 0})
data2 = data2.fillna({'pH': 1})
data2 = data2.fillna({'sulphates': 1})
data2 = data2.fillna({'alcohol': 0})

print ('Number of NaN values after replacement: ', np.sum(np.where(data2.isnull(), 1, 0)))

# Question 3
print('\nQuestion 3: \n')
data3 = data.fillna(method='ffill')
print('Sample-and-hold filling: \n', data3.iloc[16:19,0])

# Question 4
print('\nQuestion 4: \n')
data4 = data.interpolate(method='linear')
print('Linear interpolation: \n', data4.iloc[16:19,0])

# Question 5
print('='*100)
print('\nQuestion 5: \n')
noisy_data = pd.read_csv('Lab 5/noisy-sine.csv')
# apply an moving average filter on the noisy_data with window size 5, 31 and 51
# then plot the original noisy_data along with result of the three moving average filters

# window size 5 
noisy_data5 = noisy_data.rolling(window=5).mean()
# window size 31
noisy_data31 = noisy_data.rolling(window=31).mean()
# window size 51
noisy_data51 = noisy_data.rolling(window=51).mean()

# plot the original noisy_data along with result of the three moving average filters
plt.plot(noisy_data, label='noisy-sine')
plt.plot(noisy_data5, label='moving_average_5')
plt.plot(noisy_data31, label='moving_average_31')
plt.plot(noisy_data51, label='moving_average_51')
plt.legend()
plt.show()

#Question 6
# i)
dataset = pd.read_csv("C:\\Users\\miles\\OneDrive - Queen's University\\Eng Year 3 - 2022-2023\\Sem 2\\ELEC 390\\Lab5 - Pre-Processing\\ECG-sample.csv", on_bad_lines='skip', header = None)

fig, ax = plt.subplots()
dataset.iloc[:].plot(ax=ax, linewidth=3)

ax.set_title('ECG Sample', fontsize=15)
ax.set_xlabel('Number of the window')
ax.set_ylabel('Value of the std')
ax.set_ylim(-0.005,0.31)
plt.show()

# ii)
features = pd.DataFrame(columns=['mean', 'std', 'max', 'min'])
window_size = 31
features['mean'] = dataset.iloc[:].rolling(window=window_size).mean()
features['std'] = dataset.iloc[:].rolling(window=window_size).std()
features['max'] = dataset.iloc[:].rolling(window=window_size).max()
features['min'] = dataset.iloc[:].rolling(window=window_size).min()
features = features.dropna()
print(features)

# iii)
features['std'].plot()
plt.show()
