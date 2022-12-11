import numpy as np
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import pickle

# train model with QDA

folder = 'data/color/'  
f0 = open(folder+'0othercolor.npy', 'rb')
X0 = np.load(f0)
f1 = open(folder+'1binblue_v2.npy', 'rb')
X1 = np.load(f1)
f2 = open(folder+'2otherlue.npy', 'rb')
X2 = np.load(f2)
f3 = open(folder+'3green.npy', 'rb')
X3 = np.load(f3)
f4 = open(folder+'4gray.npy', 'rb')
X4 = np.load(f4)
y0, y1, y2, y3, y4 = np.full(X0.shape[0],0), np.full(X1.shape[0],1), np.full(X2.shape[0], 2), np.full(X3.shape[0],3), np.full(X4.shape[0],4)
X, y = np.concatenate((X0,X1,X2,X3,X4)), np.concatenate((y0,y1,y2,y3,y4))


colorclassifier = QuadraticDiscriminantAnalysis()
colorclassifier.fit(X, y)

modelname = 'colorclassifier.sav'
pickle.dump(colorclassifier, open(modelname, 'wb'))
