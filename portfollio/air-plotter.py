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

import matplotlib
import pandas

filename = "/workspaces/Week-9-worksheet-and-session-2-code/portfollio/leeds-centre-air-quality.csv"

infile = open(filename, "r")
outfile = open("/workspaces/Week-9-worksheet-and-session-2-code/portfollio/leeds-centre-air-quality_out.csv", "w")

next(infile)

for line in infile:
    line = line.strip()
    parts = line.split(",")

    date = parts[0]
    average = []

    for date in parts[1:]:
        if date != "":
            average.append(float(date))

    if average == 0:
        total = 0
        for g in average:
            total += g
        average = total / len(average)


        outfile.write(f"{date},{average:.2f}\n")
    else:
        pass

infile.close()
outfile.close()