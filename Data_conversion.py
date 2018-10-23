# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 02:24:27 2018

@author: Tony
"""

f = open('data.ntrans_1.tlen_5.nitems_1.npats_100.patlen_4', 'r')   
Init_list = list()   
second_list = list()   
record_list = list()   
count = 1   #計算item之ID

for line in f.readlines():
    s=str(count)                       
    line = line.strip()                               
    Init_list=line.split()   #在讀檔後，初步將空格移除
    if(Init_list[0]==s): 
        second_list.append(Init_list[2])   #將Init_list的第二項紀錄
    else:
        record_list.append(second_list)   #在換Item之ID時，將second_list紀錄
        second_list=list()   #清空second_list
        second_list.append(Init_list[2])
        count=count+1
print(record_list)
open('Data_conv.txt', 'w').write('\n'.join('%s' %id for id in record_list))    #寫檔