#!/usr/bin/python3

import os
import pandas as pd


os.system('sudo apt-get install python3-pip')

data= pd.read_excel("test1.xlsx",sheet_name=0)
print(data)

var=os.system('sudo apt-get update')

if var == 0:
   data.iloc[0,data.columns.get_loc('asds')]='pass'
else:
   data.iloc[0,data.columns.get_loc('asds')]='fail'
print(data.head())

gr=os.system('dpkg --list|grep -i osd')

if gr ==  0:
   data.iloc[1,data.columns.get_loc('asds')]='pass'
else:
   data.iloc[1,data.columns.get_loc('ads')]='fail'
print(data)

data.to_excel("test1.xlsx",index=False)

upgrad=os.system('sudo unattended-upgrades -d')

if upgrad == 0:
   print("success")
else:
   print('failure')

store=os.system('dpkg --list | grep -i osd-proxy')

key='HOME'
curr=os.getenv(key)
print(curr)
print("------------------------------------------------")
print(dir(os))
