import os
import pandas as pd
import scipy as sp
import csv
import sys
import numpy as np
 
#read_data
vlookup_target = pd.read_csv(‘original_v1.csv',sep=",",index_col=False)
env_pval = pd.read_csv(‘original_v2.csv,sep=“,”,index_col=False)
print("Now, im reading csv file")
 
#vlookup_method
vlookup_result = pd.merge(vlookup_target, env_pval, how='left', on='GENE')
print(len(vlookup_result))

#QC_vlookup = vlookup_result.dropna(axis=0)
QC_vlookup = vlookup_result[np.isfinite(vlookup_result['Marker'])]
print(len(QC_vlookup))

print("vlookup -ing ...")
 
print("wait")
 
#write_csv_file
#And_sort_col
#for i in range(len(QC2)):
#    print(QC2.loc[[i],['variant', 'pval_left','pval_right' ]])
#QC3 = QC2.loc[[i],['variant', 'pval_left','pval_right' ]]
print("writing..csv..")
QC_vlookup.to_csv(“Results_merge.csv")
print("clear")
