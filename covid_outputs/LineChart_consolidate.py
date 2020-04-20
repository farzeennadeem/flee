import plotly.express as px
import plotly.graph_objects as go
import  plotly as py
import pandas as pd
import sys
import os
import pandas as pd
from os import walk
import glob
import fnmatch
import numpy as np

#borough = "brent"
borough = "ealing"
# borough = "harrow"
# borough = "hillingdon"
if len(sys.argv) > 1:
  borough = sys.argv[1]

path = os.path.join(os.getcwd(), "results", "eagle_hidalgo_1-18-04-2020")
print(path)
df_name = []
df_list = []
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if ".csv" in name:
            if "covid" not in name:
                if borough in name:
                    # print(name)
                    filepath = os.path.join(root, name)
                    print(filepath)
                    df = pd.read_csv(filepath, usecols=['infectious'], skiprows=np.arange(1,29))
                    #df = pd.read_csv(filepath, usecols=['infectious'])
                    df_list.append(df)
                    df_name.append(name)

df = pd.concat(df_list, axis=1, ignore_index=True)
df.columns = df_name

time = 0
df['#time']=0
for index, row in df.iterrows():
    df['#time'][index]=time
    time +=1


# fig = px.line(df, x="#time", y="susceptible", title='COVID-19 Simulation - London Borough of Brent')
# fig = px.line(df, x="#time", y="exposed", title='COVID-19 Simulation - London Borough of Brent')
# py.offline.plot(fig, filename='name.html')

# df['new cases'] = df['exposed'].diff(1) + df['infectious'].diff(1)
colors = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgrey", "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "grey", "green", "greenyellow", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgrey", "lightgreen", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue", "rebeccapurple", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen",]
fig = go.Figure()
for column in df:
    index = df.columns.get_loc(column)
    if column not in ['#time']:
        fig.add_trace(go.Scatter(x=df['#time'], y=df[column], mode='lines+markers',
                             marker=dict(
                                 size=1,
                                 color=np.random.randn(23), #set color equal to a variable
                                 colorscale='Plotly3', # one of plotly colorscales
                             ), name=column, visible=True))
# Set visible to "legendonly" to unhighlight curves.
py.offline.plot(fig, filename='{}.html'.format(borough))

# fig.add_trace(go.Bar(x=df['#time'], y=df['new cases'],
#                      name='change in # affected'))
# fig.add_trace(go.Scatter(x=df['#time'], y=df['infectious'],
#                          mode='lines+markers',
#                          name='infectious',  line=dict(color='red')))
# fig.add_trace(go.Scatter(x=df['#time'], y=df['recovered'],
#                          mode='lines+markers',
#                          name='recovered', line=dict(color='green')))
# fig.add_trace(go.Scatter(x=df['#time'], y=df['dead'],
#                          mode='lines+markers',
#                          name='dead', line=dict(color='black')))

# py.offline.plot(fig, filename='html_results/cases-{}.html'.format(sys.argv[1]))
