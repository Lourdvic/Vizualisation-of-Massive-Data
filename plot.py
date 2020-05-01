# Import librairies

import pandas as pd
import matplotlib.pyplot as plt

# load the dataset and print the first lines
data = pd.read_csv('./data/covid19-region.csv')
print(data.head())
col1 = "reg"
col2 = "nbre_hospit_corona"
x = data[[col1, col2]]
print(x.head())

# plot the dataset

plt.scatter(x[col2], x[col1], c = 'b')
plt.xlabel(col2)
plt.ylabel(col1)
plt.show()
# for saving the plot comment the plot.show() above
#plt.savefig("startplot.png")