# Copyright (c) [2020] [P.H.]

import keras
import tensorflow as tf
from keras.models import Sequential,load_model
from keras.optimizers import SGD
import numpy as np
import random


class ModelConfig:
    def __init__(self):
        self.train_loop=5
        self.batch_size=32
        self.epochs=3

class MyModel:
    def __init__(self,config,input_shape=(36,36,4),output_shape=(289)):
        self.input_shape=input_shape
        self._build_model()
        self.config=config
        
    def loadModel(self,pathfile):
        m=load_model(pathfile)#, custom_objects={'softmax_cross_entropy_with_logits': softmax_cross_entropy_with_logits})
        self.model.set_weights(m.get_weights())
    
    def writeModel(self, pathfile):
        self.model.save( pathfile)
    
    def getPredict(self,s):
        s=np.array([s])
        piv=self.model.predict(s)
        return piv[0]
    def evaluate(self,state,turn):
        a=self.state2input(state,turn)
        return self.getPredict(a)

    def state2input(self,state,turn):
        a=np.zeros((36,36,4),dtype=float)
        if turn==-1:
            turn=0
        for i in range(6):
            for j in range(6):
                a[i,j,0]=turn
                if state[i][j]==1: #white
                    a[i,j,1]=1
                elif state[i][j]==-1: #black
                    a[i,j,2]=1
                else:
                    a[i,j,3]=2 # block
        return a

    def _build_model(self):
        # sample_number=2
        # ainput=[]
        # aoutput=[]
        # for i in range(sample_number):
        #     ainput.append(np.arange(36*36*4,dtype=float).reshape(36,36,4))
        #     aoutput.append(np.arange(36*36*4,dtype=float).reshape(36,36,4))
        self.model=Sequential()
        x=keras.layers.Conv2D(8,(3,3),input_shape=self.input_shape,padding='SAME')
        self.model.add(x)
        #self.model.add(keras.layers.Dense(units=8, activation='relu'))
        self.model.add(keras.layers.Flatten())
        self.model.add(keras.layers.Dense(units=577, activation='sigmoid'))
        sgd=SGD(lr=0.01)
        self.model.compile(loss='categorical_crossentropy',optimizer=sgd)
        print(self.model.summary())

    def train(self,memory):
        n=len(memory)
        for i in range(self.config.train_loop):
            batch_size=min(self.config.batch_size,n)
            sample=random.sample(memory,batch_size)
            states=[]
            #piv=np.array([])
            piv=[]
            turn=[]
            for j in range(batch_size):
                states.append(sample[j][0])
                piv.append(sample[j][1])
                turn.append(sample[j][2])

            x=[]
            
            for j in range(batch_size):
                x.append(self.state2input(states[j],turn[j]))
            x=np.asarray(x).astype('float32')
            
            #y=np.array(piv)
            y=np.asarray(piv).astype('float32')
            var=self.model.fit(x, y, epochs=self.config.epochs,verbose=1,batch_size=batch_size)
            print(var.history)

        

if __name__=="__main__":
    # output_dim=[289] #36*8+1
    MyModel(ModelConfig())