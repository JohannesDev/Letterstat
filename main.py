import pygal


class Letter:
    symbol = 'A'
    amount = 10

def readArgv():
    pass

def readLetters(path, graphSize = 10):
    text = ""
    file = open (path, "r")
    text = file.read()
    file.close

    list = [0] * 256
    for i in range(len(text)):
        list[ord(text[i])] += 1

def showGraph(maxValues):
    print("started showGraph")
    chart = pygal.Bar()
    for i in range(len(maxValues)):
        chart.add(maxValues.symbol, maxValues.amount)
    chart.render_to_file('chart.svg')

readArgv()
readLetters("README.md", 10)
showGraph(Letter('A', 10))
