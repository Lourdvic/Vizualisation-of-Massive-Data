## Covid-19 Analysis by Country 
#Import librairies

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import sys

#COVID-19 daily-updated data from the GitHub data repository for the 2019 Novel Coronavirus 
#Visual Dashboard operated by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE).

#Load the datasets from the github repo

COVID_CONFIRMED_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
covid_confirmed = pd.read_csv(COVID_CONFIRMED_URL)

COVID_DEATHS_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
covid_deaths = pd.read_csv(COVID_DEATHS_URL)

COVID_RECOVERED_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
covid_recovered = pd.read_csv(COVID_RECOVERED_URL)

covid_confirmed_long = pd.melt(covid_confirmed,
                               id_vars=covid_confirmed.iloc[:, :4],
                               var_name='date',
                               value_name='confirmed')

covid_deaths_long = pd.melt(covid_deaths,
                               id_vars=covid_deaths.iloc[:, :4],
                               var_name='date',
                               value_name='deaths')

covid_recovered_long = pd.melt(covid_recovered,
                               id_vars=covid_recovered.iloc[:, :4],
                               var_name='date',
                               value_name='recovered')

#fusionnate the 3 dataframes

covid_df = covid_confirmed_long
covid_df['deaths'] = covid_deaths_long['deaths']
covid_df['recovered'] = covid_recovered_long['recovered']

#create active cases : confirmed - deaths - recovered

covid_df['active'] = covid_df['confirmed'] - covid_df['deaths'] - covid_df['recovered']

#Data cleaning

covid_df[['Province/State']] = covid_df[['Province/State']].fillna('')

covid_df.fillna(0, inplace=True)

covid_df.isna().sum().sum()

#save the dataframes to a csv file 

with open('covid_df.csv', mode='w') as employee_file:
    covid_df.to_csv('covid_df.csv', index=None)

pd.read_csv('covid_df.csv')

#group data by Country & State at the same time so we can have the max value for each over time 
covid_countries_df = covid_df.groupby(['Country/Region', 'Province/State']).max().reset_index()

#get the sum of the cases of every state
covid_countries_df = covid_countries_df.groupby('Country/Region').sum().reset_index()

#clean the Lat & Long 
covid_countries_df.drop(['Lat', 'Long'], axis=1, inplace=True)
covid_countries_df[covid_countries_df['Country/Region'] == "France"]

# group the country by date
covid_countries_date_df = covid_df.groupby(['Country/Region', 'date'], sort=False).sum().reset_index()

#let's focus on France
covid_FR = covid_countries_date_df[covid_countries_date_df['Country/Region'] == 'France']

# function to analyse a country info 
# by plotting a treemap of the global confirmed case 
# and the evolution of this spreading of the virus 

def plot_country_global_info(country):
    country_info = covid_countries_df[covid_countries_df['Country/Region'] == country]
    
    country_info_long = country_info.melt(value_vars=['active', 'deaths', 'recovered'],
                                          var_name="status",
                                          value_name="count")

    country_info_long['upper'] = 'Confirmed cases'
    
    fig = px.treemap(country_info_long, path=["upper", "status"], values="count",
                     title=f"Total COVID-19 confirmed cases in {country}",
                     color_discrete_sequence=['#3498db', '#2ecc71', '#e74c3c'],
                     template='plotly_dark')

    fig.data[0].textinfo = 'label+text+value'

    fig.show()

# plot the spread of the country overtime

def plot_country_cases_over_time(country, log):
    country_date_info = covid_countries_date_df[covid_countries_date_df['Country/Region'] == country]
    
    fig, ax = plt.subplots(figsize=(16, 6))

    if log:
        ax.set(yscale="log")
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:g}'.format(y)))
        plt.title("(logarithmic scale)", color='white')

    sns.lineplot(x=country_date_info['date'], y=country_date_info['confirmed'], sort=False, linewidth=2)
    sns.lineplot(x=country_date_info['date'], y=country_date_info['deaths'], sort=False, linewidth=2)
    sns.lineplot(x=country_date_info['date'], y=country_date_info['recovered'], sort=False, linewidth=2)
    sns.lineplot(x=country_date_info['date'], y=country_date_info['active'], sort=False, linewidth=2)
                
    ax.lines[0].set_linestyle("--")

    plt.suptitle(f"COVID-19 cases in {country} over the time", fontsize=16, fontweight='bold', color='white')

    plt.xticks(rotation=45)
    plt.ylabel('Number of cases')

    ax.legend(['Confirmed', 'Deaths', 'Recovered', 'Active'])

    plt.show()

#function to display it 
def get_country_covid_info(country="US", log=False):
    plot_country_global_info(country)
    
    plot_country_cases_over_time(country, log)

def loop():
    countries = ["France", "US", "Argentina", "Belgium", "Brazil", "Burkina", "China", "India", "Indonesia", "Korea", "Monaco", "Morocco", "Niger", "Portugal", "Russia", "Spain", "Tunisia", "Uruguay"]
    while True:
        print("\nConfirmed Cases visualization : \n")

        print("Please type a name of a country\n")
        print("1. Show list of available country")
        print("2. Return")
        print("3. Quit")
        choice = input("")
        if choice == "1":
            print("\nList")
            for country in countries:
                print(country)
        elif choice == "2":
            break
        elif choice == "3":
            sys.exit()
        else:
            get_country_covid_info(choice)
