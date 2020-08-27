# import csv
# import datetime
# import plotly.graph_objects as goo
# import matplotlib.pyplot as plt
# from plotly.subplots import make_subplots
# from operator import itemgetter

class finance():
    def __init__(self):
        self.data = {}
        self.graph_label = {"all": {"title":"Bank balance on:", "y":"Balance"}, "highest": {"title":"Amount spent on:", "y":"Amount Spent"} ,"month": {"title":"Amount spent per month:","y":"Amount Spent"}}

        self.format_data()

    def format_data(self):
        with open('stmt.csv', mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                if row[0] == "" or row[0] == "Date" or row[2] == "":
                    continue
                try:
                    self.data[datetime.datetime.strptime(row[0], "%m/%d/%Y")]
                except:
                    self.data[datetime.datetime.strptime(row[0], "%m/%d/%Y")] = []
                self.data[datetime.datetime.strptime(row[0], "%m/%d/%Y")].append((row[1],row[2],row[3]))

    #description|amount|balance

    def highest_data(self):
        x = []
        y = []
        text = []
        for key in list(self.data.keys()):
            self.data[key].sort(key=itemgetter(1), reverse=True)
            try:
                low = sorted(self.data[key], key=itemgetter(1))[0]
            except:
                print("no")
            text.append(
                "HIGH : $" + self.data[key][0][1] + " Gained from: " + self.data[key][0][0] + "      LOW : $" + low[1] + " Spent on: " + low[0])
            sum = 0
            x.append(key)
            for tup in self.data[key]:
                sum += float(tup[1])
            y.append(sum)
        return x,y,text

    def all_data(self):
        x = []
        y = []
        text = []
        for key in list(self.data.keys()):
            self.data[key].sort(key=itemgetter(1), reverse=True)
            # try:
            #     low = sorted(data[key], key=itemgetter(1))[0]
            # except:
            #     print("no")
            #
            # text.append(
            #     "HIGH : $" + data[key][0][1] + " Gained from:" + data[key][0][0] + "      LOW : $" + low[1] + "Spent on: " + low[0])

            for tup in self.data[key]:
                text.append(tup[0])
                y.append(float(tup[1]))
                x.append(key)
        return x,y,text

    def month_data(self):
        x = []
        y = []
        temp1 = [0,-100000]
        temp2 = [0,100000]
        text = []
        sum = 0
        mon = list(self.data.keys())[0].month
        for key in list(self.data.keys()):
            self.data[key].sort(key=itemgetter(1), reverse=True)
            if mon == 13:
                mon = 0
            if mon != key.month:
                mon += 1
                x.append(datetime.date(key.year,key.month,15))
                y.append(sum)
                text.append("HIGH : $"+temp1[1]+" Gained from: "+temp1[0]+"      LOW : $"+temp2[1]+" Spent on: "+temp2[0])
                sum = 0
            for tup in self.data[key]:
                sum += float(tup[1])
                if float(temp1[1]) < float(tup[1]):
                    temp1 = tup
                if float(temp2[1]) > float(tup[1]):
                    temp2 = tup
        return x,y,text

    def plot(self, plot):

        if plot == "month":
            x,y,text = self.month_data()
            # print(sum(y)/len(y))

        if plot == "highest":
            x,y,text = self.highest_data()

        if plot == "all":
            x,y,text = self.all_data()

        grph = goo.Figure(goo.Bar(x=x,y=y,text=text))
        grph.update_layout(
            title="{}".format(self.graph_label[plot]["title"]),
            xaxis_title="Date",
            yaxis_title="{}".format(self.graph_label[plot]["title"]),
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#7f7f7f"
            )
        )
        grph.show()

    def get_range(self, start, end):
        total = 0
        for key in list(self.data.keys()):
            if key >= start and key <= end:
                for tup in self.data[key]:
                    total += float(tup[1])
        return total

# print(get_range(data))

# fig.append_trace(highest, 2, 1)
# fig.append_trace(all, 1, 1)
#
# fig.show()
#
# months.show()
# all.show()
