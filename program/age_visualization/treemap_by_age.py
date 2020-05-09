import plotly.express as px
import pandas as pd

def treemap_by_age():
    data = pd.read_csv('data/covid19-region.csv')
    is_not_0 = data["sursaud_cl_age_corona"]!="0"
    data = data[is_not_0]
    data["all"] = "France"
    data["reg"]= data["reg"].astype(str) 
    data = data.replace({
        "reg": {
            "1": "Guadeloupe",
            "2": "Martinique",
            "3": "Guyane",
            "4": "La Réunion",
            "6": "Mayotte",
            "7": "Autre",
            "8": "Autre",
            "11": "Île-de-France",
            "24": "Centre-Val de Loire",
            "27": "Bourgogne-Franche-Comté",
            "28": "Normandie",
            "32": "Hauts-de-France",
            "44": "Grand Est",
            "52": "Pays de la Loire",
            "53": "Bretagne",
            "75": "Nouvelle-Aquitaine",
            "76": "Occitanie",
            "84": "Auvergne-Rhône-Alpes",
            "93": "Provence-Alpes-Côte d’Azur",
            "94": "Corse"
        },
        "sursaud_cl_age_corona": {
            "0": "Tous",
            "A": "Moins de 15 ans",
            "B": "15-44 ans",
            "C": "45-64 ans",
            "D": "65-74 ans",
            "E": "75 et plus",
        }
    })
    fig = px.treemap(data, path=['sursaud_cl_age_corona', 'reg'], values='nbre_pass_corona')
    fig.show()
