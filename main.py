import pygal

def readLetters():
    text = ""
    file = open ("README.md", "r")
    text = file.read()
    file.close

    list = [0] * 256
    for i in range(len(text)):
        list[ord(text[i])] += 1
    print(list)

def showGraph():
    print("started showGraph")

readLetters()
showGraph()
