import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("owid-covid-data.csv")

# use these to view data
#print(df.shape)
#print(df.columns)
#df.head()

# looking for date, location (country)
# new_cases, total_cases
# new_deaths, total_deaths
# people_vaccinated, people_fully_vaccinated
# population, continent, gdp_per_capita


# Clean and filter 
df['date'] = pd.to_datetime(df['date']) # converts date to 'datetime'

US = df[df['location'] == 'United States'] # Focus on United States

US[['new_cases', 'new_deaths', 'people_vaccinated']].isnull().sum() # checking for null values

# display plot for cases in the US
plt.figure(figsize=(12,7))
plt.plot(US['date'], US['new_cases'], label='Daily New Cases', color='red')
plt.xlabel('Date'); plt.ylabel('Cases') # Date v Cases plot
plt.legend() # set legend
plt.grid(True)
plt.title('Covid in the U.S.', fontsize=16)
plt.show() # display plot with specifications

# vaccination graph 
plt.figure(figsize=(12,7))
# partially and fully vaccinated
plt.plot(US['date'], US['people_vaccinated'], label='Vaccinated (1+ dose)', color='green')
plt.plot(US['date'], US['people_fully_vaccinated'], label='Fully Vaccinated', color='blue')
plt.title('COVID-19 Vaccination Progress in the US')
plt.xlabel('Date'); plt.ylabel('People') # Date vs People vaccinated
plt.legend()
plt.grid(True)
plt.show()

# compare multiple countries
countries = ['United States', 'India', 'Brazil', 'Germany', 'Japan', 'China', 'France']
df_subset = df[df['location'].isin(countries)]

# frequency of cases
df_subset['Frequency'] = (df_subset['total_cases'] / df_subset['population']) # Define Frequency as (total cases / population) for use in graph

fig = px.line(df_subset, x='date', y='Frequency', color='location', title='Frequency of COVID-19 Cases by Country') # Set specifications of graph 
fig.update_layout(xaxis_title="Date") # Change x axis label from date to Date
fig.show() # will pull up in web browser
