import random
import string
import os
import pandas as pd
from datetime import datetime, timedelta

def checkBalance():
    # Asks the user what month they want to know the balance for
    month = input('What is the month you want to query against? ')
    
    # Loads the csv file
    data = pd.read_csv('expenseTrack.csv', parse_dates = ['date'], dayfirst = True)

    # Calculate month data
    month_expense_data = data[(data['date'].dt.month == int(month)) & (data['category'] != "Income")]
    month_income_data = data[(data['date'].dt.month == int(month)) & (data['category'] == "Income")]    

    # Run sum
    total_sum = round(month_income_data['value'].sum() - month_expense_data['value'].sum(),2)

    print(f'The total expense for this month is: {total_sum}')

checkBalance()