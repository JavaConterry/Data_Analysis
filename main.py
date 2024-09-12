from urllib.request import urlopen
import pandas as pd

response = urlopen('https://api.openf1.org/v1/weather?csv=true&meeting_key=1237')
data = pd.read_csv(response)
data.to_csv('canadagp_2024_weather.csv')