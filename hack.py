import csv
with open('PCA_CDB_3202_F_Census.csv','rb') as f:
  reader=csv.reader(f)
  your_list=list(reader)

print your_list