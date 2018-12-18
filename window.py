from tkinter import *
from tkinter import ttk
import os
import shutil
from os import path
import sys
import fileinput


def show_entry_fields():
    i = e1.get()
    l = e2.get()
    m = e3.get()
    j=i.upper()
    k=i.capitalize()
    
    file_name =k+'_Procedure'
    update_sql_name= j+"_UPDATE_PROC.sql"
    ctl_name= j+"_CTL.ctl"
    create_shell= k+"_Create_Temp.sh"
    update_shell= k+"_Update.sh"
    create_temp_sql= k+"_Create_Temp.sql"
    update_sql= k+"_Update.sql"
    csv_name =  j+"_CSV.csv"
    #DB
    shutil.copytree('Generic_Procedure',file_name)
    print(i+'_Procedure/DB')
    os.chdir(i+'_Procedure/DB')
#DB
#ALL.SQL
    
    with open('All.sql', 'r') as file :
        filedata = file.read()
        filedata = filedata.replace('GENERIC', j)
    with open('All.sql', 'w') as file:
        file.write(filedata)
        
        
#GENERIC_UPDATE_PROC.sql

    with open('GENERIC_UPDATE_PROC.sql', 'r') as file :
        filedata = file.read()
        filedata = filedata.replace('GENERIC_UPDATE_PROC', j+'_UPDATE_PROC')
        filedata = filedata.replace('534912', l)
        filedata = filedata.replace('STATEMENT_1', m)
        filedata = filedata.replace('DP_GENERIC_TEMP', 'DP_'+j+'_TEMP')
    with open('GENERIC_UPDATE_PROC.sql', 'w') as file:
        file.write(filedata)

        
    
    
    os.rename("GENERIC_UPDATE_PROC.sql",update_sql_name)

#CTL #no file changes require in .ctl

    os.chdir("..")     
    os.chdir('Manual Steps/CTL')
    
    with open('GENERIC_CTL.ctl', 'r') as file :
        filedata = file.read()
        filedata = filedata.replace('DP_GENERIC_TEMP', 'DP_'+j+'_TEMP')
        
    with open('GENERIC_CTL.ctl', 'w') as file:
        file.write(filedata)
    
    
    os.rename("GENERIC_CTL.ctl",ctl_name)

#SHELL  #Generic_Update.sh  #Generic_Create_Temp.sh

    os.chdir("..")
    os.chdir('Shell') 
    
    #Generic_Update.sh
    with open('Generic_Update.sh', 'r') as file :
        filedata = file.read()
        filedata = filedata.replace('GENERIC', j)
        filedata = filedata.replace('Generic',k)
    with open('Generic_Update.sh', 'w') as file:
        file.write(filedata)
    #Generic_Create_Temp.sh
    with open('Generic_Create_Temp.sh', 'r') as file :
        filedata = file.read()
        filedata = filedata.replace('GENERIC_UPDATE', j+'_UPDATE')
        filedata = filedata.replace('Generic_Create_Temp',k+'_Create_Temp')
        filedata = filedata.replace('GENERIC_CSV',j+'_CSV')
        filedata = filedata.replace('GENERIC_CTL',j+'_CTL')
        filedata = filedata.replace('DP_GENERIC_TEMP', 'DP_'+j+'_TEMP')
    with open('Generic_Create_Temp.sh', 'w') as file:
        file.write(filedata)
    
        
     
    os.rename("Generic_Create_Temp.sh",create_shell)
    os.rename("Generic_Update.sh",update_shell)

#SQL

    os.chdir("..")
    os.chdir('SQL')    
    #GENERIC_UPDATE.sql
    with open('Generic_Update.sql', 'r') as file :  
        filedata = file.read()
        filedata = filedata.replace('GENERIC', j)
    with open('Generic_Update.sql', 'w') as file:
        file.write(filedata)
        
    #Generic_Create_Temp.sql
    with open('Generic_Create_Temp.sql', 'r') as file :  
        filedata = file.read()
        filedata = filedata.replace('DP_GENERIC_TEMP', 'DP_'+j+'_TEMP')
        filedata = filedata.replace('DP_GENERIC_TEMP_INDEX', 'DP_'+j+'_TEMP_INDEX')
    with open('Generic_Create_Temp.sql', 'w') as file:
        file.write(filedata)    
        
    os.rename("Generic_Create_Temp.sql",create_temp_sql)
    os.rename("Generic_Update.sql",update_sql)
#csv
    
    os.chdir("..")
    os.rename("GENERIC_CSV.csv",csv_name)
    

master = Tk()
master.title('Procedure Generator by AM.DP taam')

#tab addition
tab_control = ttk.Notebook(master)
#master.geometry('350x200')
tab_1 = ttk.Frame(tab_control)
tab_2 = ttk.Frame(tab_control)
tab_control.add(tab_1,text='Procedure')
tab_control.add(tab_2,text='About Us')
tab_control.pack(expand=1, fill='both')

#tab_2
Label(tab_2, text="developers : saif.b.ali & vinit.b.mehta").grid(row=0)


#tab_1
Label(tab_1, text="Procedure Name").grid(row=0)
Label(tab_1, text="Total number of records").grid(row=1)
Label(tab_1, text="Update statement").grid(row=2)

e1 = Entry(tab_1)
e2 = Entry(tab_1)
e3 = Entry(tab_1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(tab_1, text='Finish', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)
Button(tab_1, text='Generate Procedure', command=show_entry_fields).grid(row=5, column=0, sticky=W, pady=4)



mainloop( )

#dp team....... DEVELOPERS - saif.b.ali & vinit.a.mehta