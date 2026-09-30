#!/usr/bin/env python3

"""Basic MySQL examples matching basic-sql.ipynb (media.MOCK_DATA). Modified for Jimmy Brown's lab 4"""
import json
import os

import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# get environment variables.
DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")  
DBNAME = os.getenv("DBNAME") 

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DBNAME)
cur = db.cursor()


#function to get rows that match the value in group column
def get_data_by_group(value):
    """Return data with a value matching the input in the group column"""
    logger.info("Beginning to get data in group")
    query = "SELECT * FROM mock WHERE `group` = %s;"
    try:
        cur.execute(query, (value,))
        results = cur.fetchall()
        output = []
        for r in results:
            output.append(r)
        logger.info("Got data into group")
        return output
    except mysql.connector.Error as e:
        print("MySQL Error: ", str(e))
        logger.info("Couldn't get data into group")
        return None

#function to group data by a column and output counts for each unique value in that column
def plot_counts(groupby):
    """Count people per groupby column unique value, show a bar chart, and return the DataFrame."""
    logger.info("Starting the groupby process to count")
    query = "SELECT "+groupby+", COUNT("+groupby+") FROM mock GROUP BY "+groupby+" ;"
    try:
        cur.execute(query)
        results = cur.fetchall()
        output = []
        for r in results:
            output.append(r)
        df = pd.DataFrame(output)
        df.plot.bar(x=0, y=1)
        plt.tight_layout()
        plt.show()
        logger.info("Created visualization of the data in groups")
        return df
    except mysql.connector.Error as e:
        print("MySQL Error: ", str(e))
        logger.info("Couldn't complete groupby count for some reason.")
        return None

#creating the main function
def main():
    """Run the demo queries and close the database connection."""

    print("=== by group ===")
    print(get_data_by_group("Fantastic Four"))

    print("=== plot ===")
    plot_counts("gender")

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
