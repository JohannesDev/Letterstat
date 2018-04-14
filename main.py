import pygal
import sys, getopt

class Letter(object):
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount

#loading custom inputs from user
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


def readLetters(path, graphSize = 10):
    text = ""
    file = open (path, "r")
    text = file.read()
    file.close

    list = [0] * 256
    for i in range(len(text)):
        list[ord(text[i])] += 1

    #test output
    return [Letter("A", 10),Letter("B", 5),Letter("C", 2)]

def showGraph(maxValues, outputfile):
    print("started showGraph")
    chart = pygal.Bar()
    for i in range(len(maxValues)):
        chart.add(maxValues[i].symbol, maxValues[i].amount)
    if '.svg' in outputfile:
        chart.render_to_file(outputfile)
    elif '.png' in outputfile:
        #convert svg to png


path, graphsize, outputfile = readArgv(sys.argv[1:])
highestLetters = readLetters(path, graphsize)
showGraph(highestLetters, outputfile)
