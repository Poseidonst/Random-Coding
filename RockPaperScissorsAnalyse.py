from bokeh.plotting import figure, show, output_file
import json

def plotfile(filename, output):
    with open(filename, "r") as f:
        dict = json.load(f)

    output_file(output)
    x_categories = ["player", "computer"]
    x = ["player", "computer"]
    y = [dict["player"], dict["computer"]]
    p = figure(x_range = x_categories)
    p.vbar(x = x, top = y, width = 0.5)
    show(p)




plotfile("RPSStats.json", "RPSStats.html")
