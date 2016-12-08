# Thinkful Challenge; write a python script from sratch to isolate all cities WHERE warm_month = 'July'

import sqlite3 as lite
import pandas as pd 

con  = lite.connect('getting_started.db')

with con:
	cur = con.cursor()

	# Out with the old.
	cur = con.execute('DROP TABLE IF EXISTS cities')
	cur = con.execute('DROP TABLE IF EXISTS weather')

	# In with the new.
	cur = con.execute('CREATE TABLE cities (name text, state text)')
	cur = con.execute('CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)')

# Create data for tables cities and weather
cities = (
    ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA')
    );

weather = (
  	('New York City',   2013,    'July',        'January',     62),
  	('Boston',          2013,    'July',        'January',     59),
  	('Chicago',         2013,    'July',        'January',     59),
  	('Miami',           2013,    'August',      'January',     84),
  	('Dallas',          2013,    'July',        'January',     77),
  	('Seattle',         2013,    'July',        'January',     61),
  	('Portland',        2013,    'July',        'December',    63),
  	('San Francisco',   2013,    'September',   'December',    64),
  	('Los Angeles',     2013,    'September',   'December',    75)
  );

# Insert data into respective tables
with con:
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)

	# Join tables together and run search for July as warm_month
	cur.execute("SELECT city, warm_month FROM weather INNER JOIN cities ON name =  city WHERE warm_month = 'July'")

	#Show the data
	rows = cur.fetchall()
	df = pd.DataFrame(rows)
	print('The cities that are warmest in July are %s' % rows)
	print(df)
	


