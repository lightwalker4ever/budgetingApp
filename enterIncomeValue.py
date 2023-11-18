import random
import string
import os
import pandas as pd
import genericFunctions as gf
from datetime import datetime, timedelta

def enterIncomeValue():
    category = "Income"
    value = input("What is the value you want to add? ")
    date = input("What is the date of the income? ")
    comments = input("Any comments? ")

    gf.addRecord('expenseTrack.csv', date, value, category, comments)

enterIncomeValue()