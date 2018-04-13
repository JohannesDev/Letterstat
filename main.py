import pygal

def readArgv():
    pass
def readLetters(path, graphSize = 10):

class Letter(symbol, amount):
    pass

def readLetters():
    text = ""
    file = open ("README.md", "r")
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
readLetters()
showGraph(Letter('A', 10))
