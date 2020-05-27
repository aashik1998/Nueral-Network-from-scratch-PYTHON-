import random
import math
pi=math.pi
res=[]
x_test1=[]
x_train1=[]
x_test2=[]
x_train2=[]
y_test=[]
y_train=[]
for q in range(50):
	res.append(random.uniform(-1,1)) 
for i in range(40):
	if 0<=i<10:
		x_test1.append(res[i])
	elif 10<=i<20:
		x_train1.append(res[i])
	elif 20<=i<30:
		x_test2.append(res[i])
	else:
		x_train2.append(res[i])

print(x_test1[9])
print(x_train1[9])
print("break")
print(x_test2[9])
print(x_train2[9])

for i in range(10):
	y_train.append(6*math.sin(math.radians(pi*x_train1[i])) + math.cos(math.radians(pi*x_train2[i])))
	y_test.append(6*math.sin(math.radians(pi*x_test1[i])) + math.cos(math.radians(pi*x_test2[i])))

print("break")
print(y_test[9])
print(y_train[9])
	 