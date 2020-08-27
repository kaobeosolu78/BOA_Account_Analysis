import datetime
import plotly.graph_objects as goo
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
from operator import itemgetter

temp = []
with open("School_Data", mode="r") as f:
    for line in f.readlines():
        line = line.replace("\n","")
        line = line.replace("$","")
        try:
            temp.append([datetime.datetime.strptime(line.split("\t")[1], "%m/%d/%Y"),line.split("\t")[3],float(line.split("\t")[4])])
        except:
            pass

x = []
y = []
text = []
balance = 0
temp.sort(key=itemgetter(0))
for val in temp:
    x.append(val[0])
    text.append(val[1])
    balance += val[2]
    y.append(balance)

# [(x.append(val[0]),text.append(val[1]),y.append(val[2])) for val in temp]

highest =goo.Scatter(x=x,y=y,text=text)

highest = goo.Figure(data=highest)
highest.update_layout(
    title="Amount spent on:",
    xaxis_title="Date",
    yaxis_title="Amount Spent",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

highest.show()