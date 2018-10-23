# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 20:11:39 2018

@author: Tony
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 21:24:10 2018

@author: Tony
"""
import FP_Growth
import Data_convert_Weka
parsedDat = [line.split() for line in open('Data_conv.txt').readlines()]   #將dataset加入list
#print(parsedDat)
table=[]
table = Data_convert_Weka.table_bulid(parsedDat)
Data_convert_Weka.csv_conv(table, parsedDat, "weka.csv")
initSet = FP_Growth.createInitSet(parsedDat)   #初始set格式化
myFPtree, myHeaderTab = FP_Growth.createTree(initSet, 3)   #建FP-tree
myFreqList = []    #保存FrequentItemSet
FP_Growth.mineTree(myFPtree, myHeaderTab, 3, set([]), myFreqList)
myFPtree.show()
FP_Growth.associate(parsedDat,myFreqList)
#print(len(myFreqList))
print(myFreqList)
