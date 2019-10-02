import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

plt.style.use('bmh')
_FIG_SIZE = (16*0.6,12*0.6)

tbsp = pd.read_csv('tbsp.csv')
rates = pd.read_csv('rates.csv')

new = pd.DataFrame(tbsp['Date'].append(rates['Date']))
new.drop_duplicates(inplace=True)
new.reset_index(inplace = True, drop = True) # created 'new' dataframe with dates available for both csv files
new['Index'] = np.nan
