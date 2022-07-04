from dis import show_code
import random
import statistics
from unicodedata import name
import plotly.graph_objects as go
import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv_("StudentPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data) / len(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean +std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean +(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean +(3*std_deviation)

fig = ff.create_distplot([data], ["reading scores"], show_hist=false)
fig.add_trace(go.scatter(x=[mean, mean], y= [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.scatter(x=[first_std_deviation_start, first_std_deviation_start], y= [0, 0.17], mode = "lines", name = "STANDARD DEVIATION"))
fig.add_trace(go.scatter(x=[first_std_deviation_end, first_std_deviation_end], y= [0, 0.17], mode = "lines", name = "STANDARD DEVIATION"))
fig.add_trace(go.scatter(x=[second_std_deviation_start, second_std_deviation_start], y= [0, 0.17], mode = "lines", name = "STANDARD DEVIATION"))
fig.add_trace(go.scatter(x=[second_std_deviation_end, second_std_deviation_end], y= [0, 0.17], mode = "lines", name = "STANDARD DEVIATION"))

list_of_data_under_1_std_deviation = {result for result in data if result > first_std_deviation_start and result < first_std_deviation_end}
list_of_data_under_2_std_deviation = {result for result in data if result > second_std_deviation_start and result < second_std_deviation_end}
list_of_data_under_3_std_deviation = {result for result in data if result > third_std_deviation_start and result < third_std_deviation_end}

print("Meat of this data is", format(mean))
print("Median of this data is", format(median))
print("Mode of this data is", format(mode))
print("Standard deviation of this data is", format(std_deviation))
