import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

#plt.style.use('bmh')
#_FIG_SIZE = (16*0.6,12*0.6)

#'2018-12-19'

class CombinedData():

    def __init__(self, tbsp, rates):
        self.tbsp = pd.read_csv(tbsp)
        self.rates = pd.read_csv(rates)

    def combine(self):
        combined_df = pd.DataFrame(self.tbsp.append(self.rates))
        combined_df.drop_duplicates(inplace=True)
        # created 'new' dataframe with dates available for both csv files
        combined_df.reset_index(inplace=True, drop=True)
        cols_to_drop = [3,4,5,6] # columns to remove
        # removes needless columns
        combined_df.drop(combined_df.columns[cols_to_drop],axis=1,inplace=True)
    
        return combined_df

data = CombinedData('tbsp.csv', 'rates.csv')
print(data.combine())
