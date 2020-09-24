# loop through train matrix, create feature vector where ' ' is a 0, '#' is a 1, '+' is a 2
# check the label, create a weight vector (start with w = 0)
# multiply w[] by feature[] to get an f value
# if (f > 0 and classification == true) or (f<0 and classification == false): break
# elif f < 0 and classification == true: weights increment by their respective feature
# elif f > 0 and class == false: decrement weights

import random
import time
def getF(weights, features):
    f = 0
    #print(len(features))
    #print(len(weights))
    for i in range(len(features)):
        f += features[i] * weights[i]
    return f

def incrementW(weights, features, w):
    for i in range(len(features)):
        weights[i] += features[i]
    w+=1

def decrementW(weights, features, w):
    for i in range(len(features)):
        weights[i] -= features[i]
    w-=1

def getFeatures(plot):
    features = []
    for row in plot:
        for item in row:
            if item == ' ':
                features.append(0)
            elif item == '#':
                features.append(1)
            elif item == '+':
                features.append(2)
    return features

def getFeatureList(data):
    featureList = []
    for types in data[0]:
        for plot in types.list:
            featureList.append(getFeatures(plot))
    return featureList

def allTrue(data, featureList):
    for classif in data[0]:
        counter = 0
        for types in data[0]:
            for plot in types.list:
                features = featureList[counter]#getFeatures(plot)
                counter+=1
                if classif.label == types.label:
                    if getF(classif.weights, features) + classif.w <= 0:
                        return False
                else:
                    if getF(classif.weights, features) + classif.w >= 0:
                        return False
    return True
#gotta figure out why its giving bias to 9
    """while allTrue(data, featureList) is False and trials < 300:
        weights = []
        for classif in data[0]:
            counter = 0
            for types in data[0]:
                for plot in types.list:
                    features = featureList[counter]#getFeatures(plot)
                    counter+=1
                    if classif.label == types.label:
                        while getF(classif.weights, features) + classif.w <= 0:
                            incrementW(classif.weights, features, classif.w)
                    else:
                        while getF(classif.weights, features) + classif.w >= 0:
                            decrementW(classif.weights, features, classif.w)
            weights.append(classif.weights)
        trials+=1
        print("comepleted: " + str(trials))"""

def digitLearning(data):
    start_time = time.time()
    featureList = getFeatureList(data)
    trials = 0
    #random.shuffle(data[0])
    weights = []
    for x in data[0]:
        #print(x.label, end = " ")
        weights.append(x.weights)
    changed = True
    while changed and trials < 300:
        changed = False
        counter = 0
        for types in data[0]:
            for plot in types.list:
                features = featureList[counter]#getFeatures(plot)
                counter+=1
                subcount = 0
                for classif in data[0]:
                    if classif.label == types.label:
                        while getF(weights[subcount], features) + classif.w <= 0:
                            incrementW(weights[subcount], features, classif.w)
                            changed = True
                    else:
                        while getF(weights[subcount], features) + classif.w >= 0:
                            decrementW(weights[subcount], features, classif.w)
                            changed = True
                    subcount+=1
            #weights.append(classif.weights)
        trials+=1
        #print("comepleted: " + str(trials))

        """for types in data[0]:
            for plot in types.list:
                features = getFeatures(plot)
                if classif.label == types.label:
                    while getF(classif.weights, features) + classif.w < 0:
                        incrementW(classif.weights, features, classif.w)
                else:
                    while getF(classif.weights, features) + classif.w > 0:
                        decrementW(classif.weights, features, classif.w)"""
    """for classif in weights:
        for i in classif:
            print(i, end = " ")
        print()"""
    print(print("--- %s seconds ---" % (time.time() - start_time)))
    return weights


def digitTesting(data, weightList, testing):
    """x = data[0][0].list[0]
    features = getFeatures(x)
    solutions = []
    idx = 0
    for weight in weightList:
        #for i in weight:
        solutions.append(getF(weight, features) + data[0][idx].w)
        idx+=1
    solution = solutions.index(max(solutions))
    print(solution)
    for x in solutions:
        print(x, end=" ")
    print()"""
    if testing > -1:
        features = getFeatures(data[1][testing].list[0])
        solutions = []
        idx = 0
        for weights in weightList:
            """for i in weights:
                print(i, end=" ")
            print()"""
            x = getF(weights, features) + data[0][idx].w
            solutions.append(x)
            idx += 1
        return solutions.index(max(solutions))
        # print(solution)
        #results.append(solution)
    results = []
    for test in data[1]:
        for plot in test.list:
            features = getFeatures(plot)
            solutions = []
            idx = 0
            for weights in weightList:
                """for i in weights:
                    print(i, end=" ")
                print()"""
                solutions.append(getF(weights, features) + data[0][idx].w)
                idx+=1
            solution = solutions.index(max(solutions))
            #print(solution)
            results.append(solution)
            """for x in solutions:
                print(x, end = " ")
            print()"""
    correct = 0
    count = 0
    #print(len(results))
    with open("testlabels") as f:
        while True:
            c = f.read(1)
            if c != ' ' and c != '\n' and c != '':
                """if count>9:
                    break"""
                if int(c) == results[count]:
                    correct += 1
                count += 1

            if not c:
                break
    f.close()
    """print()
    print(correct)"""
    return correct

def subMatrix(matrix, row, col):
    res = []
    r = row
    while r < row+10:
        x = []
        c = col
        while c < col+10:
            x.append(matrix[r][c])
            c +=1
        res.append(x)
        r +=1
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


def faceLearning(data):
    start_time = time.time()
    featureList = getFaceFeatureList(data)
    """for i in featureList:
        print(i, end = " ")"""
    trials = 0
    #random.shuffle(data[0])
    """for x in data[0]:
        print(x.label, end = " ")"""
    #data[0].reverse()
    weights = [0] * 42
    changed = True
    while changed and trials < 100000:
        changed = False
        counter = 0
        #random.shuffle(data[0])
        for types in data[0]:
            random.shuffle(types.list)
            #print(types.label)
            #print("current list is len" + str(len(types.list)))
            for plot in types.list:
                features = featureList[counter]  # getFeatures(plot)
                #print(getF(weights, features))
                counter += 1
                if types.label == 1:
                    while getF(weights, features) + types.w <= 0:
                        changed = True
                        incrementW(weights, features, types.w)
                else:
                    while getF(weights, features) + types.w >= 0:
                        #print("decrement")
                        changed = True
                        decrementW(weights, features, types.w)
        #weights.append(data[0].weights)
        """for classif in data[0]:
            counter = 0
            for types in data[0]:
                for plot in types.list:
                    features = featureList[counter]#getFeatures(plot)
                    counter+=1
                    if classif.label == types.label:
                        while getF(classif.weights, features) + classif.w <= 0:
                            incrementW(classif.weights, features, classif.w)
                    else:
                        while getF(classif.weights, features) + classif.w >= 0:
                            decrementW(classif.weights, features, classif.w)"""
        trials+=1
        #print("comepleted: " + str(trials))
        """for types in data[0]:
            for plot in types.list:
                features = getFeatures(plot)
                if classif.label == types.label:
                    while getF(classif.weights, features) + classif.w < 0:
                        incrementW(classif.weights, features, classif.w)
                else:
                    while getF(classif.weights, features) + classif.w > 0:
                        decrementW(classif.weights, features, classif.w)"""
    """for classif in weights:
        for i in classif:
            print(i, end = " ")
        print()"""
    print(print("--- %s seconds ---" % (time.time() - start_time)))
    return weights

def faceTesting(data, weightList, testing):
    if testing > -1:
        test = data[1][testing].list[0]
        subs = []
        a = 0
        while a < 69:
            b = 0
            while b < 59:
                subs.append(subMatrix(test, a, b))
                b += 10
            a += 10
        features = getFaceFeatures(subs)
        solutions = []
        idx = 0
        # for weights in weightList:
        """for i in weights:
                print(i, end=" ")
            print()"""
        solutions.append(getF(weightList, features) + data[0][idx].w)
        idx += 1
        solution = solutions.index(max(solutions))
        # print(solution)
        if getF(weightList, features) + data[0][idx].w > 0:
            return 1
            # print(1)
        else:
            return 0
    #print(weightList)
    results = []
    for type in data[1]:
        features = []
        for list in type.list:
            subs = []
            a = 0
            while a < 69:
                b = 0
                while b < 59:
                    subs.append(subMatrix(list, a, b))
                    b += 10
                a += 10
            features = getFaceFeatures(subs)
            #print(x)
            #features.append(x)
            solutions = []
            idx = 0
            #for weights in weightList:
            """for i in weights:
                    print(i, end=" ")
                print()"""
            solutions.append(getF(weightList, features) + data[0][idx].w)
            idx += 1
            solution = solutions.index(max(solutions))
            #print(solution)
            if getF(weightList, features) + data[0][idx].w > 0:
                results.append(1)
                #print(1)
            else:
                results.append(0)
               # print(0)
            #results.append(solution)
            """for x in solutions:
                print(x, end=" ")
            print()"""
    correct = 0
    count = 0
    #print(len(results))
    with open("facedatatestlabels") as f:
        while True:
            c = f.read(1)
            if c != ' ' and c != '\n' and c != '':
                """if count==149:
                    break"""
                if int(c) == results[count]:
                    correct += 1
                count += 1

            if not c:
                break
    f.close()
    """print()
    print(correct)"""
    return correct
