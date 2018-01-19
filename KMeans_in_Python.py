# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:03:31 2017

@author: Jason


K-means clustering implemented in Python for a data set
Please change the link of the dataset as per your convenience.
The data set is a random download from the internet


"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy.random as rand
style.use('ggplot')
import matplotlib.patches as mpatches
import time


class KMeans(object):
    
    def __init__(self, k =2, path = "C://Users//Jason//Desktop//realdata.txt"):
        self.path = path
        self.k = k
        self.dfRD = pd.read_csv(path,names =['a','Length','Width'],sep = '\t')
        del self.dfRD['a']
    
    def initialiseClusters(self):
        self.kList = {}
        for i in range(self.k):
            randomNum = rand.randint(len(self.dfRD.index))
            self.kList[i] = (self.dfRD.iloc[randomNum][0] , self.dfRD.iloc[randomNum][1])
        #print(self.kList)
    
    #takes a list of 2 points each and gives the distance
    def distance(self,a,b):
        return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    
    
    def assignCentroid(self):
        self.kListGroup = {}
        for i in range(len(self.dfRD.index)):
            dmin = 999999999
            for j in range(len(self.kList)):
                d = self.distance(self.kList[j],(self.dfRD.iloc[i][0],self.dfRD.iloc[i][1]))
                if d < dmin:
                    dmin = d
                    group = j
            
            if group in self.kListGroup:
                self.kListGroup[group].append((self.dfRD.iloc[i][0],self.dfRD.iloc[i][1]))
            else:
                self.kListGroup[group] = [(self.dfRD.iloc[i][0],self.dfRD.iloc[i][1])]
            
    
    
    def newCentroid(self):
        self.newCentroidList ={}
        for i in range(len(self.kListGroup)):
            newx = 0
            newy = 0
            for j in range(len(self.kListGroup[i])):
                newx += self.kListGroup[i][j][0]
                newy += self.kListGroup[i][i][1]
            
            avgx = newx/len(self.kListGroup[i])
            avgy = newy/len(self.kListGroup[i])
            
            self.newCentroidList[i] = (avgx,avgy)
        if self.newCentroidList[i] == self.kList:
            return True
        else:
            self.kList = self.newCentroidList.copy()
            return False
        
    
    def displayResult(self):
        colors = 3*["r.","g.","c.","y.","m.","b."]
        markers = ["o","v","<","v","^","<",">"]
        legends = ['c1','c2','c3','c4','c5','c6']
        plt.xlabel("Length")
        plt.ylabel("Width")
        cluster1 = mpatches.Patch(color = 'red', label = "Cluster 1")
        cluster2 = mpatches.Patch(color = 'green', label = "Cluster 2")
        cluster3 = mpatches.Patch(color = 'cyan', label = "Cluster 3")
        cluster4 = mpatches.Patch(color = 'yellow', label = "Cluster 4")
        cluster5 = mpatches.Patch(color = 'magenta', label = "Cluster 5")
        cluster6 = mpatches.Patch(color = 'blue', label = "Cluster 6")
        
        clusterList = [cluster1,cluster2,cluster3,cluster4,cluster5,cluster6]
        
        x = len(self.newCentroidList)
        clusterList = clusterList[0:x]
        for i in range(len(self.kListGroup)):
            for j in range(len(self.kListGroup[i])):
                x = plt.plot(self.kListGroup[i][j][0],self.kListGroup[i][j][1],colors[i],marker=markers[i],markersize=3)  
                
            plt.plot(self.kList[i][0],self.kList[i][1],'k',marker='x',linewidth=50,markersize = 20)
        
        
        plt.legend(handles=clusterList)
        plt.show()
        


def main():
    start = time.time()
    algorithm = KMeans(k=3) 
    algorithm.initialiseClusters()
    b = False
    count = 1;
    
    while (b == False):
        algorithm.assignCentroid()
        b = algorithm.newCentroid()
        count+=1
        if count == 10:
            break;
    algorithm.displayResult()       
    end = time.time()
    print("Time measure: %.2f sec"  %(end-start))

    
if __name__ == "__main__":
    main()  
