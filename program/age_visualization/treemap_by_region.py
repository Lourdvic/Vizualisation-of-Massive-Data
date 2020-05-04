import plotly.express as px
import pandas as pd

def treemap():
    data = pd.read_csv('../data/covid19-region.csv')

    is_not_0 = data["sursaud_cl_age_corona"]!="0"
    data = data[is_not_0]
    fig = px.treemap(data, path=['reg','sursaud_cl_age_corona'], values='nbre_pass_corona')
    fig.show()
