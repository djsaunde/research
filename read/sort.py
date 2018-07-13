""" Sort read.csv files by read data column. """

import os
import pandas as pd

directories = ['books', 'papers']

for d in directories:
	f = os.path.join(d, 'read.csv')

	try:
		df = pd.read_csv(f, parse_dates=['Read'])
		df = df.sort_values(by='Read', axis='rows', ascending=True)
		df.to_csv(f, index=False)
	except pd.errors.EmptyDataError:
		continue
