'''
You have been provided with ‘leeds-central-air-quality.csv’ which is a file containing air quality data for Leeds from the last few years. There are 4 values – particulate matter (25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of air quality – which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/09/2024,68,20,25,5

You would plot a point at (68+20+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.

Name: Saloni Pradhan
Student ID: 201829493
'''

import matplotlib.pyplot as plt
import pandas as pd

filename = "leeds-centre-air-quality.csv"
filename1 = "leeds-centre-air-quality_out.csv"

infile = open(filename, "r")
outfile = open(filename1, "w")

next(infile)

outfile.write("date,average\n")

for line in infile:
    line = line.strip()
    parts = line.split(",")

    date = parts[0]
    average = []

    for i in parts[1:]:
        if i != "":
            average.append(float(i))

    if len(average) > 0:
        total = 0
        for g in average:
            total += g
        average = total / len(average)


        outfile.write(f"{date},{average:.2f}\n")
    else:
        pass

df = pd.read_csv(filename1) 
df["date"] = pd.to_datetime(df["date"], dayfirst=True)
df.plot(kind="line", x="date", y="average")
plt.xlabel = ("Date")
plt.ylabel = ("Avereage Pollution")

plt.show()

infile.close()
outfile.close()