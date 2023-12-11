import random
import string
import os
import pandas as pd
import genericFunctions as gf
from datetime import datetime, timedelta

def enterExpense():
    area = "Expense"
    category = input("What category was your expense on? ")
    value = input("What value did you spend? ")
    date_entered = input("What date did you spend? If it's today, leave this field blank: ")
    if(date_entered == ''):
        date = datetime.now()
    valid_format = False
    if(valid_format == False and date_entered != ''):
        try:
            date = datetime.strptime(date_entered, '%d/%m/%Y')
            valid_format = True
        except:
            pass
    if(valid_format == False and date_entered != ''):
        try:
            date = datetime.strptime(date_entered, '%d/%m/%y')
            valid_format = True
        except:
            pass
    if(valid_format == False and date_entered != ''):
        try:
            date = datetime.strptime(date_entered, '%Y-%m-%d')
            valid_format = True        
        except:
            pass
    if(valid_format == False and date_entered != ''):
        try:
            date = datetime.strptime(date_entered, '%y-%m-%d')
        except:
            raise ValueError("Date format is invalid.")
    comments = input("Any comments? ")
    changes_allowed = True
    timestamp_record_added = datetime.now()
    gf.addRecord('expenseTrack.csv', date.date(), value, area, category, comments, changes_allowed, timestamp_record_added)
    print(f'The following expense was added:\nDate: {date.date()}\nValue: {value}\nCategory: {category}\nComments: {comments}\n Added on the {timestamp_record_added}.' )