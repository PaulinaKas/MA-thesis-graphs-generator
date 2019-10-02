import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

plt.style.use('bmh')
_FIG_SIZE = (16*0.6,12*0.6)

tbsp = pd.read_csv('tbsp.csv')
rates = pd.read_csv('rates.csv')

appended_pd = pd.DataFrame(tbsp['Date'].append(rates['Date']))
appended_pd.drop_duplicates(inplace=True)
appended_pd.reset_index(inplace = True, drop = True) # created 'new' dataframe with dates available for both csv files
appended_pd['TBSP Index'] = np.nan
appended_pd['Interest rate'] = np.nan

print(appended_pd)
