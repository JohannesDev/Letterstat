import pygal

class Letter(object):
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount

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
        chart.add(maxValues[i].symbol, maxValues[i].amount)
    chart.render_to_file('chart.svg')

readArgv()
readLetters("README.md", 10)

highestLetters=  [Letter("A", 10),Letter("B", 5),Letter("C", 2)]
showGraph(highestLetters)
