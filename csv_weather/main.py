import csv

with open("weather_data.csv") as file:
    full_data = csv.reader(file)
    data = list(full_data)[1:]
    temperatures = list(map(lambda row: row[1], data))
    print(temperatures)