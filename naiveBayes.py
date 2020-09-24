
import extractFeatures
import math

def subMatrix(matrix, row, col):
    res = []
    """print(row)
    print(col)"""
    r = row
    while r < row+10:
        x = []
        c = col
        while c < col+10:
            x.append(matrix[r][c])
            c +=1
        res.append(x)
        r +=1
    """for a in res:
        print(a)"""
    return res

def getFaceFeatures(list):
    res = []
    for sub in list:
        count = 0
        for row in sub:
            for item in row:
                if item == '#':
                    count+=1
        res.append(count)
    return res

def getFaceFeatureList(data):
    features = []
    for type in data[0]:
        for list in type.list:
            subs = []
            a = 0
            while a < 69:
                b = 0
                while b < 59:
                    subs.append(subMatrix(list, a, b))
                    b += 10
                a += 10
            x = getFaceFeatures(subs)
            #print(x)
            features.append(x)
    return features

def probDC(type, index, data):
    if type == "digit":
        result = []
        #print("checking image: " + str(index))
        test = data[1][index].list[0]
        """for row in test:
            for item in row:
                print(item, end = " ")
            print()"""
        for classif in range(10):
            features = [[0 for col in range(len(test[row]))] for row in range(len(test))]
            for row in range(len(test)):
                for col in range(len(test[row])):
                    listLen = 0
                    xCount = 0
                    while(listLen < len(data[0][classif].list)):
                        #if index == 1:
                            #print(listLen)
                        if test[row][col] == data[0][classif].list[listLen][row][col]:
                            features[row][col] +=1
                        listLen+=1
                        xCount+=1
            mult = 1
            for row in features:
                for item in row:
                   # \item = item/data[0][classif].count
                    mult = mult*item
            if mult != 0:
                mult = math.log10(mult)
            result.append(mult)
        return result
    if type == "face":
        result = []
        #print("checking image: " + str(index))
        test = data[1][index].list[0]
        """for row in test:
            for item in row:
                print(item, end = " ")
            print()"""
        subs = []
        a = 0
        while a < 69:
            b = 0
            while b < 59:
                subs.append(subMatrix(test, a, b))
                b += 10
            a+=10
        for classif in range(2):
            feats= [1]*42
            subInd = 0
            for x in subs:
                hits = 0
                for row in x:
                    for item in row:
                        if item == '#':
                            hits += 1
                listLen = 0
                trainHits = 0
                while listLen < len(data[0][classif].list):
                    #print("checking a list")
                    trainsubs = []
                    a=0
                    while a < 69:
                        b = 0
                        while b < 59:
                            trainsubs.append(subMatrix(data[0][classif].list[listLen], a, b))
                            b += 10
                        a += 10
                    for s in trainsubs[subInd]:
                        for item in s:
                            if item == '#':
                                trainHits+=1
                    if trainHits == hits:
                        feats[subInd]+=1
                    listLen+=1
                subInd+=1
            mult = 1
            for i in feats:
                mult = mult*i
            #print(mult)
            """if mult != 0:
                    mult = math.log10(mult)"""
            #print("found one")
            result.append(mult)
        return result
    """if type == "face":
        result = []
        print("checking image: " + str(index))
        test = data[1][index].list[0]
        subs = []
        a = 0
        while a < 69:
            b = 0
            while b < 59:
                subs.append(subMatrix(test, a, b))
                b += 10
            a+=10
        hitList = getFaceFeatures(subs)
        mult = 1
        for a in len(featureList):
            if a == len(data[0][0].list):
                result.append(mult)
                mult = 1
            
        for classif in range(2):
            feats= [1]*42
            subInd = 0
                listLen = 0
                trainHits = 0
                while listLen < len(data[0][classif].list):
                    #print("checking a list")
                    trainsubs = []
                    a=0
                    while a < 69:
                        b = 0
                        while b < 59:
                            trainsubs.append(subMatrix(data[0][classif].list[listLen], a, b))
                            b += 10
                        a += 10
                    for s in trainsubs[subInd]:
                        for item in s:
                            if item == '#':
                                trainHits+=1
                    if trainHits == hits:
                        feats[subInd]+=1
                    listLen+=1
                subInd+=1
            mult = 1
            for i in feats:
                mult = mult*i
            print("mult is: " + str(mult))

            result.append(mult)
        return result"""


def naiveBayes(data, type, testing):
   # print("Features extracted")
    """print(data[0][0].count)
    print(len(data[0][0].list))
    print(data[0][1].count)
    print(len(data[0][1].list))"""

    if testing > -1:
        DCforAllC = probDC(type, testing, data)
        probCDforAllC = []
        cCount = 0
        for c in data[0]:
            if type == "digit":
                probCD = (DCforAllC[cCount])  # *(data[0][cCount].count)
            else:
                probCD = (DCforAllC[cCount]) * len(data[0][cCount].list)  # (data[0][cCount].count)
            probCDforAllC.append(probCD)
            cCount += 1
        max_val = max(probCDforAllC)
        """for x in probCDforAllC:
                    print(x)"""
        value = probCDforAllC.index(max_val)
        return value
        #solutions.append(value)


    solutions = []
    index = 0
    for x in data[1]:
        #print(data[1][0].list[0][69][60])
        DCforAllC = probDC(type, index, data)
        probCDforAllC = []
        cCount = 0
        for c in data[0]:
            if type == "digit":
                probCD = (DCforAllC[cCount])#*(data[0][cCount].count)
            else:
                probCD = (DCforAllC[cCount])*len(data[0][cCount].list)#(data[0][cCount].count)
            #print("probCD is: " + str(probCD))
            #print("DC is : " + str(DCforAllC[cCount]))
            #print("label freq : " + str(len(data[0][cCount].list)))
            probCDforAllC.append(probCD)
            cCount+=1
        max_val = max(probCDforAllC)
        """for x in probCDforAllC:
                print(x)"""
        value = probCDforAllC.index(max_val)
        #print(value)
        solutions.append(value)
        index+=1
    count = 0
    correct = 0
    """print(len(solutions))
        for i in solutions:
            print(i, end = " ")"""
    if type == "digit":
        with open("testlabels") as f:
            while True:
                c = f.read(1)
                if c != ' ' and c != '\n' and c != '':
                    """if count>9:
                        break"""
                    if int(c) == solutions[count]:
                        correct+=1
                    count += 1

                if not c:
                    break
        f.close()
        #print()
        #print(correct)
    #print(correct / 10.0)
        return correct / 10.0
    else:
        with open("facedatatestlabels") as f:
            while True:
                c = f.read(1)
                if c != ' ' and c != '\n' and c != '':
                    """if count == 149:
                        break"""
                    if int(c) == solutions[count]:
                        correct += 1
                    count += 1
                if not c:
                    break
        f.close()
        # print()
        # print(correct)
        # print(correct / 10.0)
        return correct

"""for row in range(len(test)):
    for col in range(len(test[row])):
        for cRow in range(len(data[0][classif].list)):
            for cCol in range(len(data[0][classif].list[cRow])):
                if test[row][col] ="""

"""hMatch = 1
            sMatch = 1
            pMatch = 1
            for plot in data[0][classif].list:
                p = 0
                s = 0
                h = 0
                for row in plot:
                    for item in row:
                        #print(item, end = " ")
                        #print(plot[a][b])
                        if item == '#':
                            h+=1
                        elif item == '+':
                            p+=1
                        elif item == ' ':
                            s+=1
                    #print()
                if h == data[1][index].h:
                    #print("found an h match with label " + str(data[0][classif].label))
                    hMatch += 1
                if s == data[1][index].s:
                    #print("found a s match with label " + str(data[0][classif].label))
                    sMatch += 1
                if p == data[1][index].p:
                    #print("found a p match with label " + str(data[0][classif].label))
                    pMatch += 1
            result.append(hMatch*sMatch*pMatch)
     
     
            """
"""
features = [[0 for col in range(len(test[row]))] for row in range(len(test))]
for row in range(len(test)):
    for col in range(len(test[row])):
        print("row: " + str(row))
        print("col: " + str(col))
        if col > 50 or row > 60:
            break
        bigCount += 1
        hits = 0
        rowEnd = row + 10
        colEnd = col + 10
        trainRow = row
        trainCol = col
        for row in range(rowEnd):
            for col in range(colEnd):
                if test[row][col] == '#':
                    hits += 1
        listLen = 0
        while (listLen < len(data[0][classif].list)):
            trainHits = 0
            for trainRow in range(trainRow + 10):
                for trainCol in range(trainCol + 10):
                    if trainCol > 60:
                        break
                    print(trainRow)
                    print(trainCol)
                    if data[0][classif].list[listLen][trainRow][trainCol] == '#':
                        trainHits += 1
            # if trainHits
            trainRow -= 10
            trainCol -= 10
            if test[row][col] == data[0][classif].list[listLen][row][col]:
                features[row][col] += 1
            listLen += 1
    # print()
    for i in features:
    for a in i:
        print(a, end = " ")
    print()
    print()
    print()
    print("DSDS: " + str(bigCount))
    mult = 1
    for row in features:
    for item in row:
        # item = item/data[0][classif].count

        mult = mult * item
        # mult = (mult/data[0][classif].count)
    print("label: " + str(data[0][classif].label) + "has count" + str(data[0][classif].count))
    print(mult)"""





"""    if type == "face":
        result = []
        print("checking image: " + str(index))
        test = data[1][index].list[0]
        subs = []
        a = 0
        while a < 69:
            b = 0
            while b < 59:
                subs.append(subMatrix(test, a, b))
                b += 10
            a+=10
        for classif in range(2):
            feats= [1]*42
            subInd = 0
            for x in subs:
                hits = 0
                for row in x:
                    for item in row:
                        if item == '#':
                            hits += 1
                listLen = 0
                trainHits = 0
                while listLen < len(data[0][classif].list):
                    #print("checking a list")
                    trainsubs = []
                    a=0
                    while a < 69:
                        b = 0
                        while b < 59:
                            trainsubs.append(subMatrix(data[0][classif].list[listLen], a, b))
                            b += 10
                        a += 10
                    for s in trainsubs[subInd]:
                        for item in s:
                            if item == '#':
                                trainHits+=1
                    if trainHits == hits:
                        feats[subInd]+=1
                    listLen+=1
                subInd+=1
            mult = 1
            for i in feats:
                mult = mult*i
            print("mult is: " + str(mult))
            """"""if mult != 0:
                mult = math.log10(mult)""""""
            result.append(mult)
        return result"""
