f=open("tick.csv","w")
import csv
fw=csv.writer(f)
l=[["1"," ","2","3"],
   ["4"," ","5","6"],
   ["7"," ","8","9"],
   ["10"," ","11","12"],
   ["13"," ","14","15"]]
fw.writerow(l)
f.close()
f=open("tick.csv","r")
fr=csv.reader(f)
print(fr[0])
