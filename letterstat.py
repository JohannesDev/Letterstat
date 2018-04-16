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
    inputfile = 'README.md'
    graphsize = 10
    outputfile = 'chart.svg'
    helpText = 'Usage: letterstat.py -i <inputfile> -s <graphsize> -o <outputfile>'

    try:
        opts, args = getopt.getopt(argv,'i:s:o:',['inputfile=','graphsize=',
            'outputfile='])
    except getopt.GetoptError as err:
        print(err)
        print(helpText)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-i':
            inputfile = arg

        elif opt == '-s':
            try:
                graphsize = int(arg)
            except ValueError:
                print('Graphsize is not a number')
                sys.exit(2)

        elif opt == '-o':
            outputfile = arg

        else:
            print('Unknown argument: ' + str(opt))
            print(helpText)
            sys.exit(2)

    if graphsize < 1:
        print('Graphsize must be at least 1');
        sys.exit(2)

    return inputfile, graphsize, outputfile

# Open the file and analyse the input
def readLetters(inputfile, graphsize):
    graphsize = int(graphsize)
    text = ''

    try:
        file = open (inputfile, 'r')
        text = file.read()
        file.close

    except IOError:
        print('Could not read file: ' + inputfile)
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

# Create the .svg file and save it
def showGraph(maxValues, inputfile, outputfile):
    chart = pygal.Bar()
    chart.title = 'Characters in ' + inputfile
    for i in range(len(maxValues)):
        chart.add(maxValues[i].symbol, maxValues[i].amount)

    if '.svg' in outputfile:
        try:
            chart.render_to_file(outputfile)
        except IOError:
            print('Could not write file: ', outputfile)
            sys.exit(2)

    else:
        print("The output file must end with .svg")
        sys.exit(2)

inputfile, graphsize, outputfile = readArgv(sys.argv[1:])
highestLetters = readLetters(inputfile, graphsize)
showGraph(highestLetters, inputfile, outputfile)
print('Created ' + str(outputfile) + ' from  ' + str(inputfile) + ' sucessfully.')
