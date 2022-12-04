import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def set_bins(df, col):
    '''
    @param df: DataFrame
    @param col: column interested on get the bins
    
    @return the bins to plot histograms
    '''
    step = df[col].std() / 3
    return np.arange(df[col].min(), df[col].max() + step, step)


def plot_histogram(df, col, axvline = None):
    '''
    @param df: DataFrame
    @param col: column interested see the distribution
    @param axvline: the percentile (0 to 100) to mark a vertical line on the histogram
    
    @return the plotted histogram
    '''
    
    bins = set_bins(df, col)
    sns.histplot(x=df[col], bins=bins)
    plt.ylabel('Frequency')
    
    if (axvline):
        plt.axvline(np.percentile(df[col], axvline), color='black', linewidth=2)