import pygal


def readArgv():
    pass
def readLetters(path, graphSize = 10):
    text = ""
    file = open ("README.md", "r")
    text = file.read()
    file.close

    list = [0] * 256
    for i in range(len(text)):
        list[ord(text[i])] += 1
    print(list)

def showGraph():
    print("started showGraph")
    chart = pygal.Bar()                                            # Then create a bar graph object#
    chart.add('A', [20])  # Add some values
    chart.render_to_file('chart.svg')  # Write the chart in the specified file

readArgv()
readLetters()
showGraph()
