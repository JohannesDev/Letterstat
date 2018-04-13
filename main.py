import pygal

class Letter():
    symbol = ''
    amount = 0

def readLetters():
    text = ""
    file = open ("README.md", "r")
    text = file.read()
    file.close

    list = [0] * 256
    for i in range(len(text)):
        list[ord(text[i])] += 1
    print(list)

def showGraph(maxValues):
    print("started showGraph")
    chart = pygal.Bar()
    for i in range(len(maxValues)):
        chart.add('A', [20])
    chart.render_to_file('chart.svg')

readLetters()
showGraph()
