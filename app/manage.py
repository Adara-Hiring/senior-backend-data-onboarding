"""
Main module of the server file
"""

# 3rd party modules
import unittest
import argparse
from config.server import app
import pandas as pd

def run():
    app.run(debug=True)


def test():
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

def create_and_load_data():
    import sqlite3
    import csv

    cookie_scores = '../data/cookie_scores.csv'
    data_providers = '../data/data_providers.csv'
    dataprovider_cookies = '../data/dataprovider_cookies.csv'
    email_cookies = '../data/email_cookies.csv'


    sql = sqlite3.connect('example.db')
    cur = sql.cursor()

    f=open(cookie_scores,'r') # open the csv data file
    next(f, None) # skip the header row
    reader = csv.reader(f)
    cur.execute('''CREATE TABLE IF NOT EXISTS cookie_scores
                (cookie_id integer, score real)''') # create the table if it doesn't already exist            
    for row in reader:
        cur.execute("INSERT OR REPLACE INTO cookie_scores VALUES (?, ?)", row)
    f.close()
    sql.commit()

    f=open(data_providers,'r') # open the csv data file
    next(f, None) # skip the header row
    reader = csv.reader(f)
    cur = sql.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS data_providers
                (id integer, name string)''') # create the table if it doesn't already exist            
    for row in reader:
        cur.execute("INSERT OR REPLACE INTO data_providers VALUES (?, ?)", row)
    f.close()
    sql.commit()

    f=open(dataprovider_cookies,'r') # open the csv data file
    next(f, None) # skip the header row
    reader = csv.reader(f)
    cur = sql.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS dataprovider_cookies
                (dataprovider_id integer,cookie_id integer)''') # create the table if it doesn't already exist            
    for row in reader:
        cur.execute("INSERT OR REPLACE INTO dataprovider_cookies VALUES (?, ?)", row)
    f.close()
    sql.commit()

    f=open(email_cookies,'r') # open the csv data file
    next(f, None) # skip the header row
    reader = csv.reader(f)

    cur = sql.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS email_cookies
                (hash_email string,cookie_id integer)''') # create the table if it doesn't already exist            
    for row in reader:
        cur.execute("INSERT OR REPLACE INTO email_cookies VALUES (?, ?)", row)
    f.close()
    sql.commit()
    sql.close()

if __name__ == "__main__":

    commands = dict(run=run, test=test)
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=commands.keys())
    create_and_load_data()
    commands[parser.parse_args().command]()
