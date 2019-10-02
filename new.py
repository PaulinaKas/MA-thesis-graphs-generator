import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

plt.style.use('bmh')
_FIG_SIZE = (16*0.6,12*0.6)

#'2018-12-19'

class CombinedData():

    def __init__(self, tbsp, rates):
        self.tbsp = pd.read_csv(tbsp)
        self.rates = pd.read_csv(rates)

    def combine(self):
        combined_df = pd.DataFrame(self.tbsp['Date'].append(self.rates['Date']))
        combined_df.drop_duplicates(inplace=True)
        combined_df.reset_index(inplace = True, drop = True) # created 'new' dataframe with dates available for both csv files
        combined_df['TBSP Index'] = np.nan
        combined_df['Interest rate'] = np.nan
        return combined_df

data = CombinedData('tbsp.csv', 'rates.csv')
print(data.combine())
