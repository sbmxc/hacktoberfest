import pandas as pd
from scipy.special import expit
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import random


# input from file
df = pd.read_csv('data.csv', delim_whitespace=False, sep=',', header=None)
df = df.values.tolist()

# divide in test and train
train, test = train_test_split(df, test_size=0.2)
train = np.asarray(train)
test = np.array(test)

Y = train[:,72]
train = train[:,:-1]

Y_test = test[:,72]
test = test[:,:-1]

# Normalise the data set
scaler = MinMaxScaler().fit(train)
train = scaler.transform(train)

scaler = MinMaxScaler().fit(test)
test = scaler.transform(test)

Y = Y.tolist()
train = train.tolist()
Y_test = Y_test.tolist()
test = test.tolist()



# taking scaling factor = 2,10
no_of_neurons = [15,20,1];
no_of_features = 72
no_of_iterations = 4000
eta = -0.00001

# Declaring lists for weights and bias
w01 = []
b01 = []
w02 = []
b02 = []
w03 = []
b03 = []

# Function to initialise weights and bias
def init(weights,bias,index):

    features = 0
    for i in range(no_of_neurons[index]):
        ls = []
        if index==0:
            features = 72
        else:
            features = no_of_neurons[index-1]
        limit = np.sqrt(features)
        limit = 1/limit
        for j in range(features):
            ls.append(round(random.uniform(-1*limit,limit), 3))
            # ls.append(int(1))
        weights.append(ls)

    for i in range(no_of_neurons[index]):
        bias.append(round(random.uniform(-1*limit,limit), 3))
        # bias.append(int(1))


# Calling the init() methods
init(w01,b01,0)
init(w02,b02,1)
init(w03,b03,2)
w03 = w03[0]

# Lists for plotting the graphs
X_axis = []
Y_axis = []

# Iterating doing the FF and BPA
for itr in range(no_of_iterations):
    print("iteration",itr)
    X_axis.append(itr)
    MSE = 0
    for i in range(len(train)):
        # Forward Pass
        X = train[i]
        U = np.dot(w01, X)
        U = U + b01
        H = expit(U)
        V = np.dot(w02, H)
        V = V + b02
        I = expit(V)
        W = np.dot(w03, I)
        W = W + b03
        Y_pred = expit(W)

        # BACKWARD Pass
        e = Y[i] - Y_pred
        MSE += e*e
        E = e * (Y_pred * (1 - Y_pred))

        J_b03 = E
        J_w03 = E * I
        b03 -= eta * (J_b03)
        w03 -= eta * (J_w03)

        temp = I * (1 - I)
        temp = (temp * w03)
        J_b02 = E * temp
        colu = np.reshape(np.array(temp), (np.array(temp).shape[0], 1))
        rowv = np.reshape(np.array(H), (1, np.array(H).shape[0]))
        res = np.multiply(rowv, colu)
        J_w02 = E * res
        b02 -= eta * (J_b02)
        w02 -= eta * (J_w02)

        temp2 = H * (1 - H)
        temp3 = E * np.dot(w02.transpose(), temp)  # temp * w02 * temp2
        temp3 = temp3 * temp2
        J_b01 = E * temp3
        colu = np.reshape(np.array(temp3), (np.array(temp3).shape[0], 1))
        rowv = np.reshape(np.array(X), (1, np.array(X).shape[0]))
        res = np.multiply(rowv, colu)
        J_w01 = E * res
        b01 -= eta * (J_b01)
        w01 -= eta * (J_w01)
    MSE /= len(train)
    Y_axis.append(MSE)

# Plotting the Cost Versus Iteration
plt.plot(X_axis,Y_axis)
plt.show()


# Testing
ans = 0
mean = 0
for i in range(len(test)):
    # print("Iteration ",i)
    X = test[i]
    U = np.dot(w01, X)
    U = U + b01
    H = expit(U)
    V = np.dot(w02, H)
    V = V + b02
    I = expit(V)
    W = np.dot(w03, I)
    W = W + b03
    Y_pred = expit(W)
    mean += Y_pred
    print(Y_pred,end="")
    print(Y_test[i])
    if Y_test[i]==1:
        if Y_pred >= float(0.5):
            ans += 1
    else:
        if Y_pred < float(0.5):
            ans+= 1

print("Accuracy:",ans/len(test))













