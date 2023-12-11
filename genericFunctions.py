import random
import string
import os
import pandas as pd
from datetime import datetime, timedelta

def addRecord(storage_file, date, value, area, category, comments, changes_allowed, timestamp_record_added):
    # Check if the storage file exists
    if os.path.exists(storage_file):
        with open(storage_file, 'r') as file:
            # Read all lines from the file
            stored_data = file.read().splitlines()[1:]

    else:
        # If the file doesn't exist, initialize with an empty list
        stored_data = []
    # Record
    record = f'{date},{area},{category},{value},{comments},{changes_allowed},{timestamp_record_added}'
    # Convert the data to a set
    generated_identifiers = set(stored_data)
    generated_identifiers.add(record)

    with open(storage_file, 'w') as file:
        # Write the header
        file.write("date,area,category,value,comments,changes_allowed,timestamp_record_added\n")
        # Write the unique records
        file.write('\n'.join(generated_identifiers))