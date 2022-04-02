import pandas as pd
import csv
import random 
import plotly.figure_factory as pff
import statistics
import plotly.graph_objects as go

df = pd.read_csv("devdata.csv")
data = df["average"].tolist()
mean1 = statistics.mean(data)
median2 = statistics.median(data)
mode3 = statistics.mode(data)
print(mean1)
print(median2)
print(mode3)

figure = pff.create_distplot([data],["average"],show_hist=False)
figure.show()
figure.add_trace(go.Scatter(x=[mean1,mean1],y=[0,1]))
figure.show()