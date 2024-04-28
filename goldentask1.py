# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Function for distribution graphs
def plot_distribution(df):
    for column in df.columns:
        if df[column].nunique() > 1 and df[column].nunique() < 50:
            df[column].hist()
            plt.title(f'{column}')
            plt.xlabel('Values')
            plt.ylabel('Frequency')
            plt.show()



# Function for scatter and density plots
def plot_scatter_matrix(df):
    pd.plotting.scatter_matrix(df, alpha=0.75, figsize=(10, 10))
    plt.suptitle('Scatter and Density Plot')
    plt.show()

# Read data
df1 = pd.read_csv('C:\\Users\\HP\\Downloads\\extracted\\portfolio_data.csv')

# Display basic info
print(f'Data shape: {df1.shape}')
print(df1.head())

# Visualizations
plot_distribution(df1)
plot_scatter_matrix(df1)
