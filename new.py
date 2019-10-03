import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

#plt.style.use('bmh')
#_FIG_SIZE = (16*0.6,12*0.6)

class CombinedData():

    def __init__(self, tbsp, rates):
        self.tbsp = pd.read_csv(tbsp)
        self.rates = pd.read_csv(rates)

    def combine(self):
        combined_df = pd.DataFrame(self.tbsp.append(self.rates)).groupby('Date').first()
        return combined_df

    def remove_useless_columns(self):
        thin_combined_df = self.combine()
        thin_combined_df.drop(thin_combined_df.columns[[2,3,4,5]],axis=1,inplace=True) # [2,3,4,5] are columns which should be removed
        return thin_combined_df

data = CombinedData('tbsp.csv', 'rates.csv')
data.combine()
print(data.remove_useless_columns())
