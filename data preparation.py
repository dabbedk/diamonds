import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import re

# Import mined diamond dataset
# In ggplot, diamonds categorized between "Ideal" and "Very Good" cut ratings were labeled as "Premium" which the market labels as "Excellent."
# I used string-replace to align these values to the lab-created diamond datasets.
# Added columns for "Type" and "Source" for comparitive analysis vs. lab-created diamonds.
mined = pd.read_csv('mined_diamonds.csv')

mined = mined[['carat', 'cut', 'color', 'clarity', 'price']]
mined['cut'] = mined['cut'].str.replace('Premium', 'Excellent')
mined['type'] = 'mined'
mined['source'] = 'ggplot'

# Import lab-created diamond datasets and clean up data from Clean Origin 
cleanorigin = pd.read_csv('cleanorigin_diamonds.csv', header = None)
cleanorigin.columns = ['carat', 'color', 'clarity', 'cut', 'price']
cleanorigin['price'] = cleanorigin['price'].str.replace('[$,]', '').astype(float)
cleanorigin['type'] = 'lab'
cleanorigin['source'] = 'clean origin'
cleanorigin = cleanorigin[['carat', 'cut', 'color', 'clarity', 'price', 'type', 'source']]

# Import lab-created diamond datasets and clean up data from MiaDonna
miadonna = pd.read_csv('miadonna_diamonds.csv', header = None)
miadonna.columns = ['carat', 'color', 'clarity', 'cut', 'price']
miadonna['price'] = miadonna['price'].str.replace('[$,(USD)]', '').astype(float)
miadonna['cut'] = miadonna['cut'].str.title()
miadonna['type'] = 'lab'
miadonna['source'] = 'miadonna'
miadonna = miadonna[['carat', 'cut', 'color', 'clarity', 'price', 'type', 'source']]

# Create new dataset with data from previous 3 datasets
diamonds = pd.concat([mined, cleanorigin, miadonna], ignore_index = True)
diamonds.replace('None', np.nan, inplace = True)

# Set order within categories
diamonds['cut'] = diamonds['cut'].astype('category')
diamonds['cut'].cat.reorder_categories(['Ideal', 'Excellent', 'Very Good', 'Good', 'Fair'], inplace = True)
diamonds['color'] = diamonds['color'].astype('category')
diamonds['color'].cat.reorder_categories(['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'], inplace = True)
diamonds['clarity'] = diamonds['clarity'].astype('category')
diamonds['clarity'].cat.reorder_categories(['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'], inplace = True)

# Filter diamonds only between 0.5 and 2.5 carats
diamonds = diamonds[diamonds['carat'] >= 0.5]
diamonds = diamonds[diamonds['carat'] <= 2.5]

# Calculate correlation between price / carat to justify price-per-carat variable
print('mined:', stats.pearsonr(diamonds[diamonds['type'] == 'mined']['price'], diamonds[diamonds['type'] == 'mined']['carat']))
print('lab:', stats.pearsonr(diamonds[diamonds['type'] == 'lab']['price'], diamonds[diamonds['type'] == 'lab']['carat']))

# Create Price-per-Carat column
diamonds['ppc'] = round(diamonds['price'] / diamonds['carat'], 2)

# Export dataset
diamonds.to_csv('all_diamonds.csv', index = False)