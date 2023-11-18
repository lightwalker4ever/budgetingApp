import random
import string
import os
import pandas as pd
import genericFunctions as gf
from datetime import datetime, timedelta

def enterExpenseValue():
    category = input("What category was your expense on? ")
    value = input("What value did you spend? ")
    date = input("What date did you spend? ")
    comments = input("Any comments? ")

    gf.addRecord('expenseTrack.csv', date, value, category, comments)

enterExpenseValue()