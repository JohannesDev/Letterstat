def readLetters():
    text = "Hello"
    list = [0] * 256
    for i in range(len(text)):
        list[ord(text[i])] += 1
    print(list)
    print("started readLetters")

def showGraph():
    print("started showGraph")

readLetters()
showGraph()
