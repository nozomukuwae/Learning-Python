import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
ave_temp = sum(temp_list) / len(temp_list)
print(ave_temp)