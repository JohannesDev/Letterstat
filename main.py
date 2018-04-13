import pygal

<<<<<<< HEAD

def readArgv():
    pass
def readLetters(path, graphSize = 10):
=======
class Letter():
    symbol = ''
    amount = 0

def readLetters():
>>>>>>> 34f014ce2e2bd80b827a30a44908643dffec226a
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
        chart.add('A', [20])
    chart.render_to_file('chart.svg')

readArgv()
readLetters()
showGraph()
