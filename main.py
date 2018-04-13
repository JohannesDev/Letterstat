import pygal

def readLetters():
    text = "Hello"
    list = [0] * 256
    for i in range(len(text)):
        list[ord(text[i])] += 1
    print(list)
    print("started readLetters")

def showGraph():
    print("started showGraph")
    chart = pygal.Bar()                                            # Then create a bar graph object#
    for 
    chart.add('A', [20])  # Add some values
    chart.render_to_file('chart.svg')  # Write the chart in the specified file

readLetters()
showGraph()
