# Import librairies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import plotly.express as px
import math

def percent():
    # load the dataset and print the first lines
    data = pd.read_csv('data/covid19.csv')
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

    population_by_age = {
        "0": 67063703,
        "A": 11943747,
        "B": 23972387,
        "C": 17396991,
        "D": 7377042,
        "E": 6373536,
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
            percent = datapoint[3] * 100 / population_by_age[datapoint[2]]
            age_data[datapoint[2]][0].append(percent)
            age_data[datapoint[2]][1].append(nb_date)
        # plot_data_point(datapoint, fig)
    # print(age_data)

    for key in age_data:
        plt.plot(age_data[key][1], age_data[key][0], label=age_labels[key])

    # labels = ["Var 1", "Var 2", "Var 3", "Var 4"]
    plt.title("Pourcentage de la population passé aux urgences\npour suspicion de COVID-19 par jour à partir du 24 février")
    plt.xlabel("Jour")
    plt.ylabel("Pourcentage de l'effectif")
    plt.legend()
    plt.show()
