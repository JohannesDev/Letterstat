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
    helpText = 'Usage: main.py -p <path> -s <graphsize> -o <outputfile>'

    try:
        opts, args = getopt.getopt(argv,'p:s:o:',['path=','graphsize=',
            'outputfile='])
    except getopt.GetoptError as err:
        print(err)
        print(helpText)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-p':
            path = arg
        elif opt == '-s':
            graphsize = arg
        elif opt == '-o':
            outputfile = arg
        else: 
            print('Unknown argument: ' + str(opt))
            print(helpText)
            sys.exit(2)

    return path, graphsize, outputfile

# Open the file and analyse the input
def readLetters(path, graphsize):
    graphsize = int(graphsize)
    text = ''

    try:
        file = open (path, 'r')
        text = file.read()
        file.close

    except IOError:
        print('Could not read file: ' + path)
        sys.exit(2)

    # Delte whitespaces
    text = text.replace(' ', '')
    text = text.replace('\t', '')
    text = text.replace('\n', '')

    c = Counter(text).most_common(graphsize)
    orderedLetters=[]

    if len(c) < graphsize: 
        print('Not enaught charcters in file. Reduced graphsize from ' + 
                str(graphsize) + ' to ' + str(len(c)) + '.')
        graphsize = len(c)

    for i in range(0, graphsize):
        orderedLetters.append(Letter(c[i][0], c[i][1]))

    return orderedLetters

# Create the .svg file
def showGraph(maxValues, inputfile, outputfile):
    chart = pygal.Bar()
    chart.title = 'Characters in ' + inputfile
    for i in range(len(maxValues)):
        chart.add(maxValues[i].symbol, maxValues[i].amount)
        
    if '.svg' in outputfile:
        chart.render_to_file(outputfile)

path, graphsize, outputfile = readArgv(sys.argv[1:])
highestLetters = readLetters(path, graphsize)
showGraph(highestLetters, path, outputfile)
print('Created ' + str(outputfile) + ' from  ' + str(path) + ' sucessfully.')
