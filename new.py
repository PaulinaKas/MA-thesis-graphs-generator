import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

plt.style.use('bmh')
_FIG_SIZE = (16*0.6,12*0.6)

class CombinedData():

    def __init__(self, tbsp, rates):
        self.tbsp = pd.read_csv(tbsp)
        self.rates = pd.read_csv(rates)

    def combine(self):
        combined_df = pd.DataFrame(self.tbsp.append(self.rates)).groupby('Date', as_index=False).first()
        return combined_df

    def remove_useless_columns(self):
        thin_df = self.combine()
        thin_df.drop(thin_df.columns[[3,4,5,6]],axis=1,inplace=True) # [3,4,5,6] are columns which should be removed
        return thin_df

class Graphs(CombinedData):

    def prepare_lines_for_chart(self):
        final_df = super().remove_useless_columns()
        x_ticks_labels = list(final_df.iloc[:,0])[::80] # displays every eighty date
        x = np.arange(len(final_df.iloc[:,0]))

        #s1 = savgol_filter(df_final['Stopa'], 25, 1)
        fig, ax1 = plt.subplots(figsize=_FIG_SIZE)
        s1 = final_df.iloc[:,1] # 1 means 2nd column (1st column was with dates)
        l1, = ax1.plot(x, s1, 'b-')
        ax1.title.set_text('Chart\'s title')
        ax1.set_xlabel('X label')
        ax1.set_ylabel("Y1 label", color = 'b')
        ax1.set_xticks(x[::80]) # should be the same as frequency for x_ticks_labels
        ax1.set_xticklabels(x_ticks_labels, rotation='vertical')


        ax2 = ax1.twinx()
        s2 = final_df.iloc[:,2] # 2 means 3rd column (1st column was with dates)
        l2, = ax2.plot(x, s2, 'g-')
        ax2.set_ylabel("Y2 label", color = 'g')

        return [l1, l2, fig]

    def save_chart(self):
        # defines needed values which have been returned in prepare_lines_for_chart()
        l1 = self.prepare_lines_for_chart()[0]
        l2 = self.prepare_lines_for_chart()[1]
        fig = self.prepare_lines_for_chart()[2]

        plt.legend([l1, l2], ['Y1', 'Y2'])
        fig.tight_layout()
        plt.savefig("graph.png",bbox_inches='tight',dpi=300)



data = CombinedData('tbsp.csv', 'rates.csv')
data.combine()
data.remove_useless_columns()

graph = Graphs('tbsp.csv', 'rates.csv')
graph.prepare_lines_for_chart()
graph.save_chart()
