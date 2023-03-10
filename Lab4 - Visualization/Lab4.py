import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

# This lab includes 2 main components. First, our goal is to visualize a widely used ‘Heart Disease
# Dataset’ to get some high-level information about the distribution of the data. Next, we aim to
# apply PCA and t-SNE on another widely used dataset called the ‘wine quality dataset’, with the
# foal of performing dimensionality reduction.

# Question 1
#Read the data from the csv file, and separate the labels from the data
dataset = pd.read_csv("C:\\Users\\miles\\Downloads\\heart.csv")
# Separate the labels from the data
labels = dataset.iloc[:,13]
# Separate the data from the labels
data = dataset.iloc[:,:13]

print (labels)
print (data)

# Creating a plot witha 4x4 grid of subplots, with a size of 20x10
fig, ax = plt.subplots(ncols=4, nrows=4, figsize= (20,10))

# Plotting the histograms of the data
data.hist(ax=ax.flatten()[:13])
fig.tight_layout()
plt.show()

#Question 2 - Written Response

#Question 3 - Stacked Histogram Plots implementation
dataset = pd.read_csv("C:\\Users\\miles\\Downloads\\heart.csv")
labels = dataset.iloc[:,13]
data = dataset.iloc[:,:13]
print (labels)
print (data)
fig, ax = plt.subplots(ncols=4, nrows=4, figsize= (20,10))

for i in range(0,13):
    ax.flatten()[i].hist(data.iloc[:13])
    ax.flatten()[i].set_title(data.columns.all(), fontsize=15)

fig.tight_layout()
plt.show()

#Question 4 Continuous Histogram Plots implementation
dataset = pd.read_csv("C:\\Users\\miles\\Downloads\\heart.csv")
labels = dataset.iloc[:,13]
data = dataset.iloc[:,:13]
print (labels)
print (data)
fig, ax = plt.subplots(ncols=4, nrows=4, figsize= (20,10))

data.plot(ax=ax.flatten()[:13], kind='density', subplots=True, sharex=False)

fig.tight_layout()
plt.show()

#Question 5 - Box Plot implementation
dataset = pd.read_csv("C:\\Users\\miles\\Downloads\\heart.csv")
labels = dataset.iloc[:,13]
data = dataset.iloc[:,:13]
print (labels)
print (data)
fig, ax = plt.subplots(ncols=4, nrows=4, figsize= (20,10))

data.plot(ax=ax.flatten()[:13], kind='box', subplots=True, sharex=False, sharey=False)

fig.tight_layout()
plt.show()

#Question 6 - Scatter Matrix Plot implementation
dataset = pd.read_csv("C:\\Users\\miles\\Downloads\\heart.csv")
labels = dataset.iloc[:,13]
data = dataset.iloc[:,:13]
print (labels)
print (data)
fig, ax = plt.subplots(ncols=13, nrows=13, figsize= (30,30))

pd.plotting.scatter_matrix(data, ax=ax)

fig.tight_layout()
plt.show()

#Question 7 - Written Response

#Question 8 - PCA and t-SNE analysis for the wine dataset
dataset = pd.read_csv("C:\\Users\\miles\\Downloads\\winequalityN.csv")
labels = dataset.iloc[:,12]
data = dataset.iloc[:,1:12]

for i in range(len(labels)):
    if labels[i] >7:
        labels[i] = 1
    else:
        labels[i] = 0
         
pca = PCA(n_components=2)
tsne = TSNE(n_components=2, perplexity=30)
sc = StandardScaler()

data = sc.fit_transform(data)
pca_data = pca.fit_transform(data)
tsne_data = tsne.fit_transform(data)

fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(10,10))
colors = ['green','red']
my_legends = [0, 1]

for i in range(len(my_legends)):
    ax1.scatter(pca_data[labels == i, 0], pca_data[labels == i, 1], c=colors[i], s =60)    
    ax2.scatter(tsne_data[labels == i, 0], tsne_data[labels == i, 1], c=colors[i], s =60)    
   
ax1.set_title('PCA')
ax2.set_title('t-SNE')
plt.show()

# Question 9 - PCA and t-SNE analysis for the wine dataset continued
data_set = pd.read_csv("C:\\Users\\miles\\Downloads\\winequalityN.csv")
labels = data_set.iloc[:,12]
data = data_set.iloc[:,1:12]

for i in range(len(labels)):
    if labels[i] >7:
        labels[i] = 1
    else:
        labels[i] = 0
       
pca = PCA(n_components=11)
sc = StandardScaler()

data = sc.fit_transform(data)
pca_data = pca.fit_transform(data)
fig, ax = plt.subplots(figsize=(10,10))
colors = ['green','red']
my_legends = [0, 1]

for i in range(len(my_legends)):
    ax.scatter(pca_data[labels == i, 7], pca_data[labels == i, 8], c=colors[i], s =60)    
   
ax.set_title('PCA')
plt.show()
# Question 10 - Written Response