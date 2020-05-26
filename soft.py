import numpy as np

x=np.array([[ 0.5076573985501027 , -0.43321446381724504 ] ,
[ 0.5983564653427766 , -0.2131243223537791 ] ,
[ -0.5404117433013091 , -0.28172226547189916 ] ,
[ -0.38355713175360817 , 0.0393125323990442 ] ,
[ 0.080081143348401 , 0.40810141912227316 ] ,
[ -0.40446079275834457 , -0.946667446064708 ] ,
[ -0.5210282579766288 , 0.9638124710119766 ] ,
[ 0.6712258519529495 , -0.3087155072232126 ] ,
[ -0.32593458468739933 , -0.016290662713048132 ] ,
[ 0.5259922606373748 , 0.3331624215000295 ] ])


y=np.array([[ 1.1667089189969362 ] ,
[ 1.1967477947398009 ] ,
[ 0.8221183735760539 ] ,
[ 0.8738217399799308 ] ,
[ 1.0260952083975619 ] ,
[ 0.8656017813848624 ] ,
[ 0.8272158152329123 ] ,
[ 1.2206313428708147 ] ,
[ 0.8927771284474013 ] ,
[ 1.1728536799451177 ] ])


syn0 = 2*np.random.random((2,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)

    return 1/(1+np.exp(-x))




k0 = x
k1 = nonlin(np.dot(k0, syn0))
k2 = nonlin(np.dot(k1, syn1))    


for j in range(10000):
    k0 = x
    k1 = nonlin(np.dot(k0, syn0))
    k2 = nonlin(np.dot(k1, syn1))
    k2_error = y - k2
    print("mean absolute Error:" + str(np.mean(np.abs(k2_error))))
    k2_delta = k2_error*nonlin(k2, deriv=True)
    k1_error = k2_delta.dot(syn1.T)
    k1_delta= k1_error * nonlin(k1,deriv=True)
    syn1 = syn1+k1.T.dot(k2_delta)
    syn0 =syn0+k0.T.dot(k1_delta)


xaxis=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
import matplotlib.pyplot as plt
plt.plot(xaxis,k2,label="Output")
plt.plot(xaxis,y,label="Correct Output")
plt.title("mean absolute Error:" + str(np.mean(np.abs(k2_error))))    
plt.xlabel("xaxis")
plt.ylabel("yaxis")
plt.legend()
plt.show()
