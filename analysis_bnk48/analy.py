import json
from sklearn import datasets, linear_model
from sklearn.svm import SVR
from sklearn.model_selection import KFold
from sklearn.utils import shuffle as sf
import matplotlib.pyplot as plt
dataX = json.load(open('reaction_Cleaned.json'))
dataY = json.load(open('growth_Cleaned.json'))

def splitGroup(x,y):
    tempX = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    tempY = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    num = range(len(x))
    num = sf(num)
    for (i,j) in zip(x,y):
        tempX[i[0]].append(i[2:10])
        tempY[j[0]].append(j[1])
    return tempX,tempY

def findEf(x,y):
    name = {
        '0' : 'tarwarn','1' : 'satchan','2' : 'pupe','3' : 'pun','4' : 'paim','5' : 'orn','6' : 'noey','7' : 'nink','8' : 'namsai',
        '9' : 'namneung','10' : 'music','11' : 'mobile','12' : 'miori','13' : 'mind','14' : 'maysa','15' : 'korn','16' : 'kate',
        '17' : 'kaimook','18' : 'kaew','19' : 'jib','20' : 'jennis','21' : 'jane','22' : 'ja','23' : 'izutarina','24' : 'cherprang',
        '25' : 'can'
    }
    # index = range(0,18)
    # pred = 0
    idx = 0 
    for (i,j) in zip(x,y):
        reg = linear_model.LinearRegression(fit_intercept=True)
        reg = reg.fit(i,j)
        co = list(map(lambda x : abs(x),reg.coef_))
        COEF = (sorted(zip(co,[ i for i in range (len(co))]),reverse=False))
        print(COEF,name[str(idx)])
        # pred = reg.predict(i)
        # plt.figure()
        # plt.scatter(index, pred, color='darkorange', label='data')
        # plt.scatter(index, j, color='green', label='data')
        # plt.plot(index, pred, color='navy',lw=1, label='RBF model')
        # plt.title(name[str(idx)])
        # plt.savefig(name[str(idx)])
        # plt.close()
        idx += 1

x,y = splitGroup(dataX,dataY)
findEf(x,y)
