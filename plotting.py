from motion_detector import df

from bokeh.plotting import figure, show, output_file

p=figure(x_axis='datetime', height=100, width=500, responsive=True, title= "Motion Graph")

q=p.quad(left=["Start"], right=["End"], bottom=0, top=1, color="green")
output_file("graph.html")
show(p)