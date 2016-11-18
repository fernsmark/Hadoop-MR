import pandas as pd
import pygal
from pygal.style import LightStyle

render = pd.read_csv("op.csv")

#Bar Chart
bar_chart = pygal.Bar(style=LightStyle, width=800, height=600, legend_at_bottom=True, human_readable=True, title='Locations where Earthquake magnitude was between 3.0 & 6.0')

for index, row in render.iterrows():
    bar_chart.add(row["location"], row["magnitude	"])
	
bar_chart.render_to_file('render_bar.svg')


#Line chart
# the count array will hold a list of daily counts, the label array will hold our x-axis labels
counts = []
labels = []

line_chart = pygal.Line()

for index, row in render.iterrows():
    counts.append( int( row["magnitude	"] ) )
    labels.append( row["location"].encode("utf8") ) # PyGal no like uni-code ...

# set the title of our chart to something intelligent
line_chart.title = 'Locations where Earthquake magnitude was between 3.0 & 6.0'

# set our x-axis labels, as well as the values to be shown on the graph
line_chart.x_labels = labels
line_chart.add('', counts)
	
line_chart.render_to_file('render_line.svg')