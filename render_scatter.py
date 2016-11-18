import pandas as pd
import pygal
from pygal.style import LightStyle

render = pd.read_csv("op.csv")

#Scatter Plot
xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Depth versus Magnitude where Earthquake magnitude was between 3.0 & 6.0'
for index, row in render.iterrows():
        xy_chart.add('', [(row["location"], row["magnitude      "])])
xy_chart.render_to_file('render_scatter.svg')
