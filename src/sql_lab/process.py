import os
import logging
import mysql.connector
import pandas as pd

#start the logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


#get environment variables
variable_set = {
	"host": os.getenv('DBHOST'),
	"database": os.getenv('DBNAME'),
	"user": os.getenv('DBUSER'),
	"password": os.getenv('DBPASS'),
}

#define function to read data
def read_data(filename):
	"""Reading in the data from the filename"""
	csv_output = pd.read_csv(filename)
	logger.info("I read the data")
	return csv_output

#define function to clean data
def clean_data(data):
	"""Outputted cleaned data without any nulls"""
	data_cleaned = data.dropna()
	logger.info("I cleaned the data")
	return data_cleaned

#define a function to identify what data type to pass into sql based on the python input, to be used in the loading data function
def sql_type(series):
	"""Function to help do the loading"""
	if pd.api.types.is_integer_dtype(series):
		return "BIGINT"
	if pd.api.types.is_float_dtype(series):
		return "DOUBLE"
	return "TEXT"

# define a function to load the data
def load_data(data, table):
	"""Loadong the data into a table"""
	logger.info("Starting the loading process")
	conn = None
	cursor = None
	try:
		conn = mysql.connector.connect(**variable_set)
		cursor = conn.cursor()
		col_defs = ", ".join(f"`{c}` {sql_type(data[c])}" for c in data.columns)
		cursor.execute(f"CREATE TABLE IF NOT EXISTS `{table}` ({col_defs})")
		col_names = ", ".join(f"`{c}`" for c in data.columns)
		placeholders = ", ".join(["%s"] * len(data.columns))
		insert_sql = f"INSERT INTO `{table}` ({col_names}) VALUES ({placeholders})"
		clean = data.astype(object).where(data.notna(), None)
		for row in clean.itertuples(index=False, name=None):
			cursor.execute(insert_sql, row)
		conn.commit()
		logger.info("I inserted %d rows into %s", len(data), table)
	except Exception:
		logger.exception("I couldn't load data into %s", table)
		raise
	finally:
		if cursor is not None:
			cursor.close()
		if conn is not None:
			conn.close()
			logger.info("I closed the connection")

def main():
	filename = "~/Downloads/UVA/Second year/SEM 1/DS 2022/lab-04-sql/MOCK_DATA.csv"
	data = read_data(filename)
	clean = clean_data(data)
	load_data(clean,"mock")

if __name__ == "__main__":
	main()
