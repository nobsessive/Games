# Copyright (c) [2020] [P.H.]

from collections import deque
from MonteCarloTree import MCTS,MCTconfig
from GameRules import GR
from count import GameSignal,Count
import numpy as np
import copy
import pickle
import os


class BrainMemory:
    def __init__(self, max_size,param=None):
        self.HOME_PATH=param
        self.memory_dir=os.path.join(self.HOME_PATH,"memory")
        self.max_size=max_size
        self.usable_memory = deque(maxlen=max_size)
        self.tmp_memory = deque(maxlen=max_size)
    
    def write2disk(self,mem_number=0):
        name=os.path.join(self.memory_dir,str(mem_number).zfill(8)+'.p','wb')
        pickle.dump(self.usable_memory,open(self.memory_dir))

    def addOneFrame(self, state, piv,turn):
        self.tmp_memory.append([state,piv,turn])

    def buildUsableMemory(self,winner,reward):
        while len( self.tmp_memory)>0:
            t=self.tmp_memory.pop()
            if t[2]==winner:
                t[1]=t[1][:-1]+[reward]
            self.usable_memory.append(t)
        self.tmp_memory=deque(maxlen=self.max_size)


class Brain:
    def __init__(self,param=None):
        self.HOME_PATH=param
        self.mct=MCTS(5,MCTconfig())
        self.gr=GR()
        self.gcnt=Count()
        self.epsilon=0.3 # epsilon greedy
        self.mem=BrainMemory(50,self.HOME_PATH)

    def getAction(self,cmd): # cmd.body==(board,turn)
        state=cmd.body[0].copy()
        turn=cmd.body[1]
        winner=cmd.body[2]
        if len(cmd.body[3])>0:
            othercmd=cmd.body[3]
            if othercmd[0]==1: # write model
                p=os.path.join(self.HOME_PATH,"lucas_model")
                self.mct.nn.writeModel(p)
            elif othercmd[0]==2: # read model
                p=os.path.join(self.HOME_PATH,"lucas_model")
                self.mct.nn.loadModel(p)
            return GameSignal(2,None)

        if len(winner)>0:
            self.winnerKnown(winner[0])
            self.mct.nn.train(self.mem.usable_memory)
            newsig=GameSignal(2,None)
            return newsig

        self.gcnt.incrs()
        self.mct.addRoot(copy.deepcopy(state),turn)
        pi,v=self.mct.getPiV()
        pi=np.array(pi)
        actn_list=pi[:,0]
        v_list=pi[:,1]
        m=np.argwhere(v_list==max(v_list))

        # epsilon greedy
        if np.random.random()<self.epsilon:
            m=np.random.randint(0,len(actn_list))
        
        m=actn_list[m]
        actn=int(m+0.5)
        move=self.gr.actn2move(actn,state,turn)
        self.gcnt.incrs()
        newsig=GameSignal(1,move)

        pi=[0]*577
        j=0
        for i in actn_list:
            k=int(i+0.5)
            pi[k]=v_list[j]
            j+=1

        self.mem.addOneFrame(state,pi,turn)
        
        return newsig

    def winnerKnown(self,winner):
        self.mem.buildUsableMemory(winner,self.mct.config.maxPossibleReward)
    def selfLearn(self,cmd):
        state=cmd[1][0]
        turn=cmd[1][1]
        mcts.addRoot(state,turn)
        pi,v=mcts.getPiV()
        pi=np.array(pi)
        ## -- ....
        move=gr.getMoveWithActn(state,turn,m)
        return move

    def observe(self,state):
        pass

if __name__=="__main__":
    br=Brain()