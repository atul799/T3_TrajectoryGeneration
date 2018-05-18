# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:00:38 2018

@author: atpandey
"""
#%%
import os
#list of srt files

lista=os.listdir()
lista.sort()
def process_transcript(fname):
    with open(fname) as ff:
        for line in ff:
            line=line.rstrip()
            if len(line) ==0 or len(line) <= 2:
                pass
            elif (line[2]==':'):
                pass
            else:
                print(line,end=' ')
    ff.close()
        
#%%
#fname='1 - 01 L Lesson Overview - lang_en_vs1.srt','
fname=lista[0]
print(fname)
print("*******************")
#print("operating on",fname)
process_transcript(fname)


#%%
#1:10 are 10-19
print(lista[1:11])
#%%
#2 - 02 L The Motion Planning Problem - lang_en_vs1.srt'


fname=lista[11]
print(fname)
print("*******************")
process_transcript(fname)

#%%
#12:13  are 20 and 21
print(lista[12:14])
#%%
#3 - 03 L Properties Of Motion Planning Algorithsm - lang_en_vs1.srt'
fname=lista[14]
print(fname)
print("*******************")
process_transcript(fname)

#%%
##4 - Types of Motion Planning Algorithms - lang_en_vs1.srt'
fname=lista[15]
print(fname)
print("*******************")
process_transcript(fname)

#%%
#5 - A_ - Artificial Intelligence for Robotics - lang_en_vs1.srt'
fname=lista[16]
print(fname)
print("*******************")
process_transcript(fname)
#%%
#Japanese" 5 - A_ - Artificial Intelligence for Robotics - lang_ja_vs1.srt

#fname=lista[17]
#print(fname)
#print("*******************")
#process_transcript(fname)

#%%
# Russian 5 - A_ - Artificial Intelligence for Robotics - lang_ru_vs1.srt'
#fname=lista[18]
#print(fname)
#print("*******************")
#process_transcript(fname)

#%%
#6 - 06 L A- Reminder Solution - lang_en_vs1.srt
fname=lista[19]
print(fname)
print("*******************")
process_transcript(fname)

#%%
#7 - Hybrid A_ Introduction - lang_en_vs1.srt
fname=lista[20]
print(fname)
print("*******************")
process_transcript(fname)
#%% 
#8 - 09 L Hybrid A- Tradeoffs Solution - lang_en_vs1.srt
fname=lista[21]
print(fname)
print("*******************")
#print("operating on",fname)
process_transcript(fname)
#%%
#9 - 10 L Hybrid A- In Practice - lang_en_vs1.srt
fname=lista[22]
print(fname)
print("*******************")
process_transcript(fname)

#%%
#10 - 15 L EnvironmentClassification - lang_en_vs1.srt
fname=lista[1]
print(fname)
print("*******************")
process_transcript(fname)

#%%
#11 - 16 L Frenet Reminder - lang_en_vs1.srt
fname=lista[2]
print(fname)
print("*******************")
process_transcript(fname)

#%%
#12 - 17 L The Need For T - lang_en_vs1.srt
fname=lista[3]
print(fname)
print("*******************")
process_transcript(fname)

#%%
#13 - 18 L  S D And T - lang_en_vs1.srt
fname=lista[4]
print(fname)
print("*******************")
process_transcript(fname)

#%%
#14 - 20 L Structures Trajectory Generation Overview - lang_en_vs1.srt
fname=lista[5]
print(fname)
print("*******************")
process_transcript(fname)

#%%
#15 - 21 L TrajectoriesWithBoundaryConditions - lang_en_vs1.srt
fname=lista[6]
print(fname)
print("*******************")
process_transcript(fname)


#%%
#16 - 22 Jerk Minimizing Trajectories - lang_en_vs1.srt
fname=lista[7]
print(fname)
print("*******************")
process_transcript(fname)


#%%
#17 - 23 L DerivationOverview - lang_en_vs1.srt
fname=lista[8]
print(fname)
print("*******************")
process_transcript(fname)

#%%
#18 - 25 L How Polynomial Trajectory Generation Works - lang_en_vs1.srt
fname=lista[9]
print(fname)
print("*******************")
process_transcript(fname)

#%%
#19 - 27 L WhatShouldBeCheckedSolution - lang_en_vs1.srt
fname=lista[10]
print(fname)
print("*******************")
process_transcript(fname)

#%%
#20 - 29 L Implementing Feasibility - lang_en_vs1.srt
fname=lista[12]
print(fname)
print("*******************")
process_transcript(fname)

#%%
#21 - 35 L Conclusion - lang_en_vs1.srt
fname=lista[13]
print(fname)
print("*******************")
process_transcript(fname)