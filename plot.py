# Import librairies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# load the dataset and print the first lines
data = pd.read_csv('./data/covid19-region.csv')
print(data.head())
col1 = "reg"
col2 = "nbre_hospit_corona"
x = data[[col1, col2]]
print(x.head())
# 1] Choose the number of cluster (k) & Select random centroids for each cluster

# Nb of clusters
k = 3

# Select random observation as centroids

centroids = (x.sample(n = k))
plt.scatter(x[col2], x[col1], c = 'b')
plt.scatter(centroids[col2], centroids[col1], c = 'r')
plt.xlabel(col2)
plt.ylabel(col1)
plt.show()
plt.savefig("startplot.png")