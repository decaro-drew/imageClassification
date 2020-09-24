class Digit:
    def __init__(self):
        self.type = ""
        self.label = -1
        self.count = 0
        self.h = 0
        self.p = 0
        self.s = 0
    #plot = [[] for i in range(20)]
        self.list = []
        self.labelLine = []
        self.imageLine = []
        self.weights = [0]*600
        self.w = 0
    #list = [[]for i in range(20)]

def extractDigitFeatures():
    tLabels = []
    trainDigits = []
    for i in range(10):
        dig = Digit()
        dig.label = i
        dig.type = "train"
        trainDigits.append(dig)
    with open("traininglabels") as f:
        appendcount = 0
        while True:
            c = f.read(1)
            if c != ' ' and c != '\n' and c != '':
                tLabels.append(int(c))
                appendcount+=1
                for i in trainDigits:
                    if i.label == int(c):
                        i.count += 1
            """if appendcount == 1000:
                break"""
            if not c:
                break
    f.close()

    # extract features from trainingimages
    label = -1
    counter = 0
    plot = [[] for i in range(20)]
    with open("trainingimages", "r") as f:
        #print("getting training features")
        appendcount = 0
        lineCounter= 0
        digcounter = 0
        notEmptycounter = 0
        c = 0
        h = 0
        p = 0
        s = 0
        for line in f:
            if '#' in line or '+' in line:
                notEmptycounter+=1
            if '#' not in line and '+' not in line and digcounter>19 and notEmptycounter>0:
                digcounter = 0
                notEmptycounter = 0
                found = False
                for x in trainDigits:
                    if x.label == label:
                        found = True
                        break
                if found:
                    x.list.append(plot)
                    appendcount+=1
                    #print("label: " +str(x.label))
                    """for a in plot:
                        for y in a:
                            print(y, end = " ")
                        print()"""
                    x.h += h
                    x.p += p
                    x.s += s
                    x.labelLine.append(counter)
                    x.imageLine.append((lineCounter))
                label = -1
                c = 0
                h = 0
                p = 0
                s = 0
                plot = [[] for i in range(20)]
                #plot = [[] for i in range(20)]
            elif notEmptycounter>0:
                digcounter+=1
                if c == 0:
                    label = tLabels[counter]
                    #print("counter is: " + str(counter))
                    counter+=1
                #plot.append(line)
                #print(line)
                lCoun = 0
                for i in line:
                    """print("c is: " + str(c))
                    print(i, end='')"""
                    #print(c)
                    plot[c].append(i)
                    if i == '#':
                        h += 1
                    if i == '+':
                        p += 1
                    if i == ' ':
                        s += 1
                    lCoun+=1
                c += 1

            lineCounter += 1
            """if appendcount == 1000:
                break"""
    f.close()

    #extract features from testimages
    testDigits = []
    appendcount = 0
    lineCounter = 0
    digcounter = 0
    notEmptycounter = 0
    c = 0
    h = 0
    p = 0
    s = 0
    with open("testimages", "r") as f:
        #print("getting test features")
        lineCounter= 0
        for line in f:
            """if appendcount == 10:
                break"""
            if '#' in line or '+' in line:
                notEmptycounter+=1
            if '#' not in line and '+' not in line and digcounter>19 and notEmptycounter>0:
                digcounter = 0
                notEmptycounter = 0
                if c!= 0:
                    x = Digit()
                    x.list.append(plot)
                    x.h += h
                    x.p += p
                    x.s += s
                    testDigits.append(x)
                    appendcount+=1
                c = 0
                h = 0
                p = 0
                s = 0
                plot = [[] for i in range(20)]
                #plot = [[] for i in range(20)]
            elif notEmptycounter > 0:
                digcounter += 1
                if c == 0:
                    counter += 1
                #plot.append(line)
                for i in line:
                    plot[c].append(i)
                    if i == '#':
                        h += 1
                    if i == '+':
                        p += 1
                    if i == ' ':
                        s += 1
                c += 1

            lineCounter += 1
    f.close()
    result = [[]for i in range(3)]
    for x in trainDigits:
        result[0].append(x)
    for x in testDigits:
        result[1].append(x)
    for x in tLabels:
        result[2].append(x)

    count =0
    for x in result[0]:
        count+= len(x.list)
    #result[1] = testDigits
    return result

class face:
    def __init__(self):
        self.count = 0
        self.label = -1
        self.list = []
        self.weights = [0]*42
        self.w = 0

def extractFaceFeatures():
    trainFaces = []
    x = face()
    x.label = 0
    trainFaces.append(x)
    x = face()
    x.label = 1
    trainFaces.append(x)
    tLabels = []
    with open("facedatatrainlabels") as f:
        while True:
            c = f.read(1)
            if c != ' ' and c != '\n' and c != '':
                tLabels.append(int(c))
                #appendcount += 1
                for i in trainFaces:
                    if i.label == int(c):
                        i.count += 1
                """if appendcount == 1000:
                    break"""
            if not c:
                break
    f.close()

    # extract features from trainingimages
    label = -1
    counter = 0
    plot = [[] for i in range(70)]
    c=0
    with open("facedatatrain", "r") as f:
       # print("getting face training features")
        appendcount = 0
        lineCounter = 0
        digcounter = 0
        for line in f:
            if digcounter > 69:
                digcounter = 0
                #notEmptycounter = 0
                found = False
                for x in trainFaces:
                    if x.label == label:
                        found = True
                        break
                if found:
                    x.list.append(plot)
                    appendcount += 1
                label = -1
                c = 0
                plot = [[] for i in range(70)]

                # plot = [[] for i in range(20)]
            #else:
            digcounter += 1
            if c == 0:
                label = tLabels[counter]
                # print("counter is: " + str(counter))
                counter += 1
            # plot.append(line)
            # print(line)
            lCoun = 0
            for i in line:
                """print("c is: " + str(c))
                print(i, end='')"""
                # print(c)
                plot[c].append(i)
                lCoun += 1
            c += 1
            lineCounter += 1
            """if appendcount == 1000:
                break"""
    f.close()

    c = 0
    testFaces = []
    plot = [[] for i in range(70)]
    with open("facedatatest", "r") as f:
      #  print("getting test features")
        lineCounter= 0
        for line in f:
            if digcounter > 69:
                digcounter = 0
                notEmptycounter = 0
                if c!= 0:
                    x = face()
                    x.list.append(plot)
                    testFaces.append(x)
                    appendcount+=1
                c = 0
                plot = [[] for i in range(70)]
                #plot = [[] for i in range(20)]
            #else:
            digcounter += 1
            if c == 0:
                counter += 1
            #plot.append(line)
            for i in line:
                plot[c].append(i)
            c += 1
            lineCounter += 1
    f.close()
    result = [[] for i in range(3)]
    for x in trainFaces:
        result[0].append(x)
    for x in testFaces:
        result[1].append(x)
    for x in tLabels:
        result[2].append(x)
    """count = 0
    for x in result[0]:
        count += len(x.list)"""
    # result[1] = testDigits
    return result