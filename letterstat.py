import pygal
import sys, getopt
from collections import Counter

class Letter(object):
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount

#loading custom inputs from user
def readArgv(argv):
    inputfile = 'README.md'
    graphsize = 10
    outputfile = 'chart.svg'

    try:
        opts, args = getopt.getopt(argv,"i:s:o:",["inputfile=","graphsize=","outputfile="])
    except getopt.GetoptError:
        print('main.py -i <inputfile> -s <graphsize> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-i':
            inputfile = arg
        elif opt == '-s':
            graphsize = arg
        elif opt == '-o':
            outputfile = arg

    return inputfile,graphsize,outputfile

def readLetters(inputfile, graphsize):
    graphsize = int(graphsize)

    text = ""
    file = open (inputfile, "r")
    text = file.read()
    file.close

    c = Counter(text).most_common(graphsize)
    orderedLetters=[]
    for i in range(0,graphsize):
        orderedLetters.append(Letter(c[i][0],c[i][1]))
    return orderedLetters

def showGraph(maxValues, outputfile):
    print("started showGraph")
    chart = pygal.Bar()
    for i in range(len(maxValues)):
        chart.add(maxValues[i].symbol, maxValues[i].amount)
    if '.svg' in outputfile:
        chart.render_to_file(outputfile)

inputfile, graphsize, outputfile = readArgv(sys.argv[1:])
highestLetters = readLetters(inputfile, graphsize)
showGraph(highestLetters, outputfile)
