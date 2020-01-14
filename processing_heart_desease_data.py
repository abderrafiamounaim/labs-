import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("LONG_B.csv",delimiter=';')   
            
O=[]
for i in range(0,2000,10):
    O.append(df[i:i+10])
G=[]
for j in range(0,200):
    G.append((O[j].to_numpy()).tolist())
List=[[]for k in range(0,200)]
for i in range(0,200):
    for j in range(0,10):
        List[i] += G[i][j]

data = pd.DataFrame(List)
#print(data.head(15))
#data = data.drop([77,78,79,7,55,50,51,52,53,54],axis=1)
data.columns=["id","ccf","age","sex","painloc","painexer", "relrest","delete",	"pncaden",	"cp"	
          ,"testbps",	"htn",	"chol",	"smoke"	,"cigs",	"years"	
          ,"fbs"	,"dm"	,"famhist"	,"restecg"	,"ekgmo"	,"ekgday"	
          ,"akgyr"	,"dig"	,"prop"	,"nitr"	,"pro"	,"diuretic"	,"proto"	
          ,"thaldur"	,"thaltime"	,"met"	,"thalach"	,"thalrest"	
          ,"tpeakbps"	,"tpeakpd"	,"dummy"	,"trestbpd", "exang"
          ,"xhypo",	"oldpeak"	,"slope"	,"rldv5"	,"rldv5e","ca"
          ,"restckm",	"exerckm"	,"restef"	,"restwm"	,"exerf"
          ,"exerwm","thal","thalsev","thalpul","earlobe","cmo","cday","cyr"
          ,"num","lmt","ladprox","laddist","diag","cxmain","ramus","om1"
          ,"om2","rcaprox","rcadist","lvx1","lvx2","lvx3","lvx4","lvf","cathef"
          ,"junk","name","a","b","c",]

#export_csv = data.to_csv (r'C:\Users\abderrafia\Desktop\BI\project data\project data\heart-disease\heart-disease-long-b5.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path

#data=data.drop(columns=['e'],axis=1)
def missing_data(d):
    T=d.isnull().sum().sort_values(ascending=False)
    percentage = (round(d.isnull().sum()/d.isnull().count()*100, 1)).sort_values(ascending=False)
    return ( pd.concat([T, percentage], axis=1, keys=['Total', '%']))

data1=data.drop(columns=["a","b","c","delete"])
#export_csv = data.to_csv (r'C:\Users\abderrafia\Desktop\BI\project data\project data\heart-disease\Long_b.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path

export_csv = data1.to_csv (r'C:\Users\abderrafia\Desktop\BI\project data\project data\heart-disease\heart-disease-long-beach-data.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path

print(missing_data(data1).head(15))

print(data1.head())
