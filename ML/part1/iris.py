from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

iris = datasets.load_iris()
x = iris.data[0:100] #เลือกมาเฉพาะชนิดที่ 1 และ 2 
y = iris.target[0:100]

# for i in range(len(x[0])): #แต่ละ sample จะมี feature อยู่ 4 ชนิด
#     plt.figure()
#     plt.plot(x[0:50,i],'^r',x[50:100,i],'^g')
# plt.show() #visualization feature 

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3 )
#แบ่ง train test ออกเป็น 2 ส่วน test size อยู่ที่ 30%
clf = linear_model.SGDClassifier()
#init classsifier เป็น SGDClassifier 
clf = clf.fit(x_train,y_train)
#fit model 
pred = clf.predict(x_test)
#predict

score = 0 
for idx,(i,j) in enumerate(zip(pred,y_test)):
    if(i == j):
        score = score + 1
score = (score/len(y_test))*100
#คำนวณความแม่นยำทั้งหมด
print(score) 
print('helloworld')
print('why so lag')