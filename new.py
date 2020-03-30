import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from abc import ABC, abstractmethod

plt.style.use('bmh')
_FIG_SIZE = (16*0.6,12*0.6)

class Merger(ABC):

    def __init__(self, file1, file2, *args):
        self.file1 = pd.read_csv(file1)
        self.file2 = pd.read_csv(file2)

    @abstractmethod
    def merge(self):
        pass

class FilesMerger(Merger):

    def __init__(self, *args):
        super().__init__(*args)

    def merge(self):
        merged_df = pd.DataFrame(self.file1.append(self.file2)).groupby('Date', as_index=False).first()
        return merged_df

class UselessColumnsRemover():

    def __init__(self, df_to_modify):
        self.df_to_modify = df_to_modify

    def remove_useless_columns(self):
        self.df_to_modify.drop(self.df_to_modify.columns[[3,4,5,6]],axis=1,inplace=True) # [3,4,5,6] are columns which should be removed
        # df_to_modify.iloc[:,1] = df_to_modify.iloc[:,1].interpolate(method='akima') # interpolation lets curve to be smooth, usuful for data like monthly inflation
        return self.df_to_modify

class Generator(ABC):

    @abstractmethod
    def generate_chart(self):
        pass

class ChartGenerator(Generator):

    def __init__(self, df_for_chart):
        self.df_for_chart = df_for_chart

    def generate_chart(self):
        x_ticks_labels = list(self.df_for_chart.iloc[:,0])[::80] # displays every eighty date
        x = np.arange(len(self.df_for_chart.iloc[:,0]))

        fig, ax1 = plt.subplots(figsize=_FIG_SIZE)
        s1 = self.df_for_chart.iloc[:,1] # 1 means 2nd column (1st column was with dates)
        l1, = ax1.plot(x, s1, 'b-')
        ax1.title.set_text('Chart\'s title')
        ax1.set_xlabel('X label')
        ax1.set_ylabel("Y1 label", color = 'b')
        ax1.set_xticks(x[::80]) # should be the same as frequency for x_ticks_labels
        ax1.set_xticklabels(x_ticks_labels, rotation='vertical')

        ax2 = ax1.twinx()
        s2 = self.df_for_chart.iloc[:,2] # 2 means 3rd column (1st column was with dates)
        l2, = ax2.plot(x, s2, 'g-')
        ax2.set_ylabel("Y2 label", color = 'g')

        plt.legend([l1, l2], ['Y1', 'Y2'])
        fig.tight_layout()
        plt.savefig("chart.png",bbox_inches='tight',dpi=300)

def main():
    data_merger = FilesMerger('file1.csv', 'file2.csv')
    joined_data = data_merger.merge()

    columns_remover = UselessColumnsRemover(joined_data)
    final_df = columns_remover.remove_useless_columns()

    chart_generator = ChartGenerator(final_df)
    chart_generator.generate_chart()

if __name__ == "__main__":
    main()
