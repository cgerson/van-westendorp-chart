import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# NOTE: ChartObject expects a CSV in which four fields contain one of the following strings in its name: 'cheap','bargain','getting expensive', 'too expensive'. See "example_data.csv" for an example.

class ChartObject:

    def __init__(self, pricing_data_file_path):
        
        self.pricing_data_file_path = pricing_data_file_path
        self.process_data()
        self.style = 'seaborn-darkgrid'

    def validate_file(self):
        
        # file should be a csv file
        assert "." in self.pricing_data_file_path, "Invalid file type"
        assert "csv" == self.pricing_data_file_path.split(".")[-1], "Invalid file type"
        assert os.path.exists(self.pricing_data_file_path) == True, "File not found"

        return True

    def check_pricing_progression(self, row):
        
        if row['cheap'] <= row['bargain'] <= row['getting expensive'] <= row['too expensive']:
            return True
        return False

    def process_data(self):

        self.validate_file()

        df = pd.read_csv(self.pricing_data_file_path, index_col=None)
        print "size:", len(df)
        print

        # standardize column names
        cols = ['cheap','bargain','getting expensive', 'too expensive']
        cols_mapping = {}
        for col in cols:
            try:
                k = filter(lambda x: col in x, df.columns)[0]
            except IndexError:
                print "Data must have four columns containing the following strings respectively: 'cheap','bargain','getting expensive', 'too expensive'\n\nPlease rename columns and try again." 
            cols_mapping[k] = col
        df.rename(columns = cols_mapping, inplace=True)
        
        # remove outliers
        for col in cols:
            print col
            print "size before outlier removal:", len(df)
            df = df[np.abs(df[col]-df[col].mean())<=(3*df[col].std())]
            print "size after outlier removal:", len(df)
            print

        # remove illogical responses
        self.final_df = df[df.apply(lambda x: self.check_pricing_progression(x), 
                                axis=1)].reset_index(drop=True)
        self.final_sample_size = len(self.final_df)
        print "size after removing illogical responses:", self.final_sample_size

    def set_style(self, style):
        
        # options: ['seaborn-darkgrid', 'seaborn-notebook', 'classic', 'seaborn-ticks', 'grayscale', 'bmh', 'seaborn-talk', 'dark_background', 'ggplot', 'fivethirtyeight', 'seaborn-colorblind', 'seaborn-deep', 'seaborn-whitegrid', 'seaborn-bright', 'seaborn-poster', 'seaborn-muted', 'seaborn-paper', 'seaborn-white', 'seaborn-pastel', 'seaborn-dark', 'seaborn-dark-palette']
        self.style = style

    def plot(self, intersection = "range", title = "Untitled", chart_path = "pricing_chart.png", annotate = False, PMC_coords = None, PME_coords = None, OPP_coords = None):

        '''
        Parameters:
        -----------
        * intersection: str
            > "range" (default): range of acceptable prices. the columns "bargain" and "getting expensive" responses will be flipped on the chart 
            > "opp": optimal price point. the columns "cheap" and "bargain" will be flipped
        * title: str, default 'Untitled'
        * annotate: boolean, default False
        * chart_path: str, default "pricing_chart.png"
        * OPP_coords: tuple, coordinates where OPP is found to annotate chart. Will display if annotate == True
        * PMC_coords: tuple, coordinates where PMC is found to annotate chart. Will display if annotate == True
        * PME_coords: tuple, coordinates where PME is found to annotate chart. Will display if annotate == True

        '''

        cols = ['cheap','bargain','getting expensive', 'too expensive']

        # set columns to be inverted
        assert intersection in ["range", "opp"], "invalid intersection value. possible intersection values: 'range' or 'opp'"
        if intersection == "range":
            cols_inverted = ['bargain','getting expensive']
        elif intersection == "opp":
            cols_inverted = ['cheap','bargain']

        # calc cumulative dist
        for col in cols:
            cum_sum = "{0}_cum_sum".format(col)
            cum_perc = "{0}_cum_perc".format(col)
            if col in cols_inverted:
                self.final_df[cum_sum] = self.final_df[col].sort_values(ascending=False).cumsum()
            else:
                self.final_df[cum_sum] = self.final_df[col].sort_values(ascending=True).cumsum()
            self.final_df[cum_perc] = 100*self.final_df[cum_sum]/self.final_df[col].sum()

        # plot
        plt.style.use(self.style)
        from matplotlib import rcParams
        rcParams['font.family'] = 'serif'

        fig, ax = plt.subplots(figsize=(14, 9))
        
        fig.suptitle("Van Westendorp Price Sensitivity Meter: {0}".format(title), fontsize=16, ha='center')

        for i, col in enumerate(cols):
            cum_perc = "{0}_cum_perc".format(col)
            if col in cols_inverted: 
                label = "{0} (inverted)".format(col)
            else:
                label = col
            ax.plot(self.final_df[[col,cum_perc]].sort_values(by=col).set_index(col), label=label)

        plt.title("\n{0} Responses".format(self.final_sample_size), fontsize=12, ha='center')
        plt.legend(loc='best', fontsize=14)
        plt.xlabel("$ Price", fontsize=14)
        start, end = ax.get_xlim()
        plt.xticks(np.arange(start, end+1, 5.0))
        ax.set_ylim(ymin=0, ymax=100)
        vals = ax.get_yticks()
        ax.set_yticklabels(['{:1.0f}%'.format(x) for x in vals])
        
        if annotate == True:
            if PMC_coords:
                x,y = PMC_coords
                ax.annotate('PMC', xy=PMC_coords, xytext=(x-4, y+5), size=14, weight='bold',
                            arrowprops=dict(facecolor='black', shrink=0.05))

            if PME_coords:  
                x_1, y_1 = PME_coords
                ax.annotate('PME', xy=PME_coords, xytext=(x_1+3, y_1+2), size=14, weight='bold',
                            arrowprops=dict(facecolor='black', shrink=0.05))

            if OPP_coords:
                x_2, y_2 = OPP_coords
                ax.annotate('OPP', xy=OPP_coords, xytext=(x_2-13, y_2-1), size=14, weight='bold',
                            arrowprops=dict(facecolor='black', arrowstyle='simple'))

        if chart_path:
            plt.savefig(chart_path, bbox_inches='tight')
        
        plt.show()

        