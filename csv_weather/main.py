import pandas

data = pandas.read_csv("weather_data.csv")
max_temp = data["temp"].max()
print(max_temp)