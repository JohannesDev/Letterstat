import pygal
import sys, getopt
from collections import Counter

# Object to map every letter to a number
class Letter(object):
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount

# Loading custom inputs from user
def readArgv(argv):
    path = 'README.md'
    graphsize = 10
    outputfile = 'chart.svg'

    try:
        opts, args = getopt.getopt(argv,"p:s:o:",["path=","graphsize=","outputfile="])
    except getopt.GetoptError:
        print('main.py -p <path> -s <graphsize> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-p':
            path = arg
        elif opt == '-s':
            graphsize = arg
        elif opt == '-o':
            outputfile = arg

    return path,graphsize,outputfile

# Open the file and analyse the input
def readLetters(path, graphsize):
    graphsize = int(graphsize)

    text = ""
    file = open (path, "r")
    text = file.read()
    file.close

    # Delte whitespaces
    text = text.replace(" ", "")
    text = text.replace("\t", "")
    text = text.replace("\n", "")

    c = Counter(text).most_common(graphsize)
    orderedLetters=[]
    for i in range(0,graphsize):
        orderedLetters.append(Letter(c[i][0],c[i][1]))
    return orderedLetters

# Create the .svg file
def showGraph(maxValues, outputfile):
    chart = pygal.Bar()
    for i in range(len(maxValues)):
        chart.add(maxValues[i].symbol, maxValues[i].amount)
    if '.svg' in outputfile:
        chart.render_to_file(outputfile)

path, graphsize, outputfile = readArgv(sys.argv[1:])
highestLetters = readLetters(path, graphsize)
showGraph(highestLetters, outputfile)
print('Created ' + str(outputfile) + ' from  ' + str(path) + ' sucessfully.')
