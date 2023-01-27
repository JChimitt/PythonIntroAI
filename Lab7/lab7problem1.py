import numpy as np
import pandas as pd

# You have a series of data that represents the amount of precipitation ech 
#day for a year in a given city.
# Load data file using Pandas


rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
noNullRain = pd.read_csv('Seattle2014.csv')['PRCP'].fillna(0)

rainInches = noNullRain / 254
rainAverage = np.average(rainInches)
print("Average rain =", round(rainAverage, 4), "inches")

noNullSnow = pd.read_csv('Seattle2014.csv')['SNOW'].fillna(0)

noNegatives = pd.read_csv('Seattle2014.csv')['SNOW']._get_numeric_data()
noNegatives[noNegatives < 0] = 0

snowInches = noNegatives / 254
snowAverage = np.average(snowInches)
print("Average snow =", round(snowAverage, 4), "inches")

janRain = pd.read_csv('Seattle2014.csv')['PRCP'].head(31)
janSnow = pd.read_csv('Seattle2014.csv')['SNOW'].head(31)

janRainInches = janRain / 254
janRainAverage = np.average(janRainInches)
print("\nAverage rain in January =", round(janRainAverage, 4), "inches")
janSnowInches = janSnow / 254
janSnowAverage = np.average(janSnowInches)
print("Average snow in January =", round(janSnowAverage, 4), "inches")
