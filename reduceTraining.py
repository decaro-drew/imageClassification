import random
import extractFeatures
def limitTrainingDigits(data, limit):
    if limit == 5000:
        return data
    resData = data
    trainDigits = []
    for x in range(10):
        dig = extractFeatures.Digit()
        dig.label = x
        dig.type = "train"
        trainDigits.append(dig)
    tmp = []
    for type in data[0]:
        for list in type.list:
            tmp.append(list)
    #print("length: " + str(len(tmp)))
    for x in range(limit):
        rand = random.randint(0,4999)
        #print(rand)
        dig = tmp[rand]
        if rand <= 479:
            trainDigits[0].list.append(dig)
        elif rand <= 1042:
            trainDigits[1].list.append(dig)
        elif rand <= 1530:
            trainDigits[2].list.append(dig)
        elif rand <= 2023:
            trainDigits[3].list.append(dig)
        elif rand <= 2558:
            trainDigits[4].list.append(dig)
        elif rand <= 2992:
            trainDigits[5].list.append(dig)
        elif rand <= 3493:
            trainDigits[6].list.append(dig)
        elif rand <= 4043:
            trainDigits[7].list.append(dig)
        elif rand <= 4505:
            trainDigits[8].list.append(dig)
        else:
            trainDigits[9].list.append(dig)
    resData[0] = trainDigits
    return resData



def limitTrainingFaces(data, limit):
    if limit == 150:
        return data
    resData = data
    trainFaces = []
    x = extractFeatures.face()
    x.label = 0
    trainFaces.append(x)
    x = extractFeatures.face()
    x.label = 1
    trainFaces.append(x)
    tmp = []
    for type in data[0]:
        for list in type.list:
            tmp.append(list)
    #print("length: " + str(len(tmp)))
    for x in range(limit):
        rand = random.randint(0,449)
       # print(rand)
        dig = tmp[rand]
        if rand <= 234:
            trainFaces[0].list.append(dig)
        else:
            trainFaces[1].list.append(dig)
    resData[0] = trainFaces
    return resData
