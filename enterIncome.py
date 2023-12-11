import random
import string
import os
import pandas as pd
import genericFunctions as gf
import datetime

def enterIncome():
    # User enters income amount
    area = "Income"
    category = "Income"
    value = input("What is the value you want to add? ")
    get_month_year = input("What is the month and year of the income? Leave blank if the month is the current month. Use format mm/yyyy, mm-yyyy or mm.yyyy otherwise: ")
    if get_month_year == '':
        get_month = datetime.now().month
        get_year = datetime.now().year
    elif get_month_year.__contains__("/"):
        get_month_year_split = get_month_year.split("/")
    elif get_month_year.__contains__("-"):
        get_month_year_split = get_month_year.split("-")
    elif get_month_year.__contains__("."):
        get_month_year_split = get_month_year.split(".")
    else:
        raise ValueError ("Month/Year is invalid. Please enter month and year as MM/YYYY or MM-YYYY or MM.YYYY.")
    get_month = get_month_year_split[0]
    get_year = get_month_year_split[1]
    date = datetime.datetime(int(get_year), int(get_month), 1).date()
    comments = input("Any comments? ")
    changes_allowed = True
    timestamp_record_added = datetime.datetime.now()
    gf.addRecord('expenseTrack.csv', date, value, area, category, comments, changes_allowed, timestamp_record_added)
    print(f'The following income was added:\nDate: {date}\nValue: {value}\nCategory: {category}\nComments: {comments}\n Added on the {timestamp_record_added}.' )    
    return date.month

def enterOrUpdateBudget(incomeMonth):
    read_budget_info = pd.read_csv('budget.csv')
    for index, row in read_budget_info.iterrows():
        category_value = row['category']
        value_value = row['value']
    overall = input(f'Do you want to add the default budget for all categories?')
    if overall.lower == "yes" or overall.lower() == "y":
        print("add the value from budget.csv")
    else:
        print("present tailored values for user to add for each category.")
