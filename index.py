import plotly.express as px
import plotly
import pandas as pd


myanmar = pd.read_json('kh.json')


fig = px.scatter_mapbox(myanmar, lat="latitude", lon="longitude", hover_name="latitude", zoom=7)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
plotly.offline.plot(fig, filename='./kh.html')
