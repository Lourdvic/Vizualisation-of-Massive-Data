#import libs

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

# we using sklearn and Linear Reg for the Prediction

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

def predictive_analysis():

    #we going to predict the future spread of the confirmed case

    COVID_CONFIRMED_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    covid_confirmed = pd.read_csv(COVID_CONFIRMED_URL)

    #we convert the wide data to a long one

    covid_confirmed_long = pd.melt(covid_confirmed,
                                id_vars=covid_confirmed.iloc[:, :4],
                                var_name='date',
                                value_name='confirmed')

                                #data cleaning

    covid_confirmed_long[['Province/State']] = covid_confirmed_long[['Province/State']].fillna('')
    covid_confirmed_long.fillna(0, inplace=True)
    covid_confirmed_long.isna().sum().sum()

    #sort values by Country and date & remove unuseful columns

    covid_countries_date_df = covid_confirmed_long.groupby(['Country/Region', 'date'], sort=False).sum().reset_index()
    covid_countries_date_df.drop(['Lat', 'Long'], axis=1, inplace=True)

    #et's take the France

    COUNTRY = 'France'

    covid_country = covid_countries_date_df[covid_countries_date_df['Country/Region'] == COUNTRY]

    #sum the days from the beginning

    days = np.array([i for i in range(len(covid_country['date']))])

    #plot it 

    days = np.array([i for i in range(len(covid_country['date']))])

    sns.lineplot(x=days, y=covid_country['confirmed'],
                markeredgecolor="#3498db", markerfacecolor="#3498db", markersize=8, marker="o",
                sort=False, linewidth=1, color="#3498db")

    plt.suptitle(f"COVID-19 confirmed cases in {COUNTRY} over the time", fontsize=16, fontweight='bold', color='white')

    plt.ylabel('Confirmed cases')
    plt.xlabel('Days since 1/22')

    plt.show()

    #plot the same but using logarithmic scale

    fig, ax = plt.subplots(figsize=(16, 6))

    ax.set(yscale="log")
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:g}'.format(y)))
    plt.title("(logarithmic scale)", color='white')

    sns.lineplot(x=days, y=covid_country['confirmed'],
                markeredgecolor="#3498db", markerfacecolor="#3498db", markersize=8, marker="o",
                sort=False, linewidth=1, color="#3498db")

    plt.suptitle(f"COVID-19 confirmed cases in {COUNTRY} over the time", fontsize=16, fontweight='bold', color='white')

    plt.ylabel('Confirmed cases')
    plt.xlabel('Days since 1/22')

    plt.show()

    # skip some unuseful days

    SKIP_DAYS = 30

    covid_country_confirmed_sm = list(covid_country['confirmed'][SKIP_DAYS:])

    covid_country_confirmed_sm[:60]

    # x will be the days and y the confirdmed cases

    X = days[SKIP_DAYS:].reshape(-1, 1)

    y = list(np.log(covid_country_confirmed_sm))

    # split our data so that we can have a train & test data

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.1,
                                                        shuffle=False)

    #create linear regression model
    #train our model thank to the fit() method

    linear_model = LinearRegression(fit_intercept=True)

    linear_model.fit(X_train, y_train)

    #use the model for prediction

    y_pred = linear_model.predict(X_test)

    #evaluation of the model

    print('MAE:', mean_absolute_error(y_pred, y_test))
    print('MSE:',mean_squared_error(y_pred, y_test))

    #linear regression formula : y = ax + b

    a = linear_model.coef_
    b = linear_model.intercept_

    #predict the next 30 days

    X_fore = list(np.arange(len(days), len(days) + 30))
    y_fore = [(a*x+b)[0] for x in X_fore]

    #go back to linear data in order to interpret it better

    y_train_l = list(np.exp(y_train))
    y_test_l = list(np.exp(y_test))
    y_pred_l = list(np.exp(y_pred))
    y_fore_l = list(np.exp(y_fore))

    #plot it 

    fig, ax = plt.subplots(figsize=(16, 6))

    sns.lineplot(x=days, y=covid_country['confirmed'],
                markeredgecolor="#2980b9", markerfacecolor="#2980b9", markersize=8, marker="o",
                sort=False, linewidth=1, color="#2980b9")

    sns.lineplot(x=X_train.reshape(-1), y=y_train_l,
                markeredgecolor="#3498db", markerfacecolor="#3498db", markersize=8, marker="o",
                sort=False, linewidth=1, color="#3498db")

    sns.lineplot(x=X_test.reshape(-1), y=y_test_l,
                markeredgecolor="#e67e22", markerfacecolor="#e67e22", markersize=8, marker="o",
                sort=False, linewidth=1, color="#e67e22")

    sns.lineplot(x=X_test.reshape(-1), y=y_pred_l,
                markeredgecolor="#f1c40f", markerfacecolor="#f1c40f", markersize=8, marker="o",
                sort=False, linewidth=1, color="#f1c40f")

    sns.lineplot(x=X_fore, y=y_fore_l,
                markeredgecolor="#2ecc71", markerfacecolor="#2ecc71", markersize=8, marker="o",
                sort=False, linewidth=1, color="#2ecc71")

    plt.suptitle(f"COVID-19 confirmed cases and forecasting in {COUNTRY} over the time", fontsize=16, fontweight='bold', color='white')

    plt.ylabel('Confirmed cases')
    plt.xlabel('Days since 1/22')

    plt.legend(['Unused train data', 'Train data', 'Test data', 'Predictions', 'Forecast'])
    plt.savefig('reg.svg', format='svg', dpi=1200)
    plt.show()