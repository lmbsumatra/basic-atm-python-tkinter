import os
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook

def login():
    xl = openpyxl.load_workbook("nag-iisa-lang-to.xlsx")
    xlSheet= xl["Sheet1"]
    
    loginUsername = input("Enter your username: ")
    loginPassword = input("Enter your password: ")
    
    for cell in xlSheet['A'] and xlSheet['B']: #Specifying which column to check for username and password in the said sheet
        # If such is cell exists, proceed to the next line otherwise continue to line 21
        if(cell.value is not None):
            # If loginUsername and loginPassword are in their corresponding columns then continue otherwise proceed to line 19
            if loginUsername in cell.value and loginPassword in cell.value: 
                print("Login Successfully")
            else:
                print("Invalid Login Username or Password")
        else: # For checking only if there are errors
            print("Column can't be found")
    
login()
    

    
    
