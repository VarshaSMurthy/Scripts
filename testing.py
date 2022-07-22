#!/usr/bin/python3
import sys
import os
import socket
from subprocess import DEVNULL, STDOUT, check_call
import pandas as pd
import xlrd

os.system('sudo apt-get install python3-pip')

data= pd.read_excel("test1.xlsx",sheet_name=0)
print(data)



loc=("/home/vss9kor/Documents/test1.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
print(sheet.cell_value(0,0))

print(socket.gethostname())
print("\t")
print("                  ---------------------------------------------------------        ")
print("\t \t")
#print(dir(subprocess))
def update_func():

    vari=os.system('sudo apt-get update')
    print(vari)
update_func()
print("\t")
print("                  ---------------------------------------------------------        ")
print("\t")

def upgrade_function():
    os.system('sudo apt-get upgrade')
upgrade_function()
print("\t")
print("                  ----------------------------------------------------------       ")
print("\t")

os.system('sudo unattended-upgrades -d')
print("\t")
print("                  ----------------------------------------------------------       ")
print("\t")

os.system('dpkg --list|grep -i osd')

print("\t")
print("                 ----------------------------------------------------------         ")
print("\t")

os.system('klist')

print("\t")
print("                 ----------------------------------------------------------         ")
print("\t")

os.system('sudo apt-get install sky')

print("\t")
print("                 ----------------------------------------------------------         ")
print("\t")

os.system('systemctl --user status proxy.service|cat') 

print("\t")
print("                 -------------------------------------------------------------         ")
print("\t")

os.system('sudo /opt/Symantec/symantec_antivirus/sav info -a')
print(" \t ")
print("                -----------------------------------------------------------         ")
print(" \t ")

os.system('sudo /opt/Symantec/symantec_antivirus/sav manage -g')
print("\t")
print("                 ----------------------------------------------------------          ")
print("\t")

os.system('sudo UpdateRights')
os.system('sudo echo asddfg')


var=os.system('elinks bosch.com| cat>/dev/null')
print(var)
