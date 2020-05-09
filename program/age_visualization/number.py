# Import librairies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import plotly.express as px
import math

def number():
    # load the dataset and print the first lines
    data = pd.read_csv('data\covid19.csv')
    data = data.to_numpy()

    fig = plt.figure()

    age_data = {
        "0": ([], []),
        "A": ([], []),
        "B": ([], []),
        "C": ([], []),
        "D": ([], []),
        "E": ([], []),
    }

    age_labels = {
        "0": "Tous",
        "A": "Moins de 15 ans",
        "B": "15-44 ans",
        "C": "45-64 ans",
        "D": "65-74 ans",
        "E": "75 et plus",
    }

    date = ""
    nb_date = 0

    for point_index in range(data.shape[0]):
        datapoint = data[point_index]
        if date != datapoint[1]:
            date = datapoint[1]
            nb_date = nb_date + 1
        if not math.isnan(datapoint[3]):
            age_data[datapoint[2]][0].append(datapoint[3])
            age_data[datapoint[2]][1].append(nb_date)

    for key in age_data:
        plt.plot(age_data[key][1], age_data[key][0], label=age_labels[key])

    plt.title("Nombre de passages aux urgences pour suspicion de COVID-19\npar jour à partir du 24 février")
    plt.xlabel("Jour")
    plt.ylabel("Nombre de passages")
    plt.legend()
    plt.show()
