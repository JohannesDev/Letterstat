import pygal
import sys, getopt

#only for testing purposes, remove later
import string, random

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


def readLetters(path, graphsize):
    text = ""
    file = open (path, "r")
    text = file.read()
    file.close

    list = [0] * 256
    for i in range(len(text)):
        list[ord(text[i])] += 1

    #test output
    #Random char: random.choice(string.ascii_letters)
    #Random number: random.randrange(100)
    highestLetters=[]
    for i in range(0,int(graphsize)):
        highestLetters.append(Letter(random.choice(string.ascii_letters), random.randrange(100)))
    return highestLetters

def showGraph(maxValues, outputfile):
    print("started showGraph")
    chart = pygal.Bar()
    for i in range(len(maxValues)):
        chart.add(maxValues[i].symbol, maxValues[i].amount)
    if '.svg' in outputfile:
        chart.render_to_file(outputfile)

path, graphsize, outputfile = readArgv(sys.argv[1:])
highestLetters = readLetters(path, graphsize)
showGraph(highestLetters, outputfile)
