# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading the data files
Hackathon_Working_Data = pd.read_csv(""C:\Users\HP\Downloads\extracted\Hackathon_Working_Data.csv"")
Hackathon_Validation_Data = pd.read_csv(""C:\Users\HP\Downloads\extracted\Hackathon_Validation_Data.csv"")
Hackathon_Ideal_Data = pd.read_csv(""C:\Users\HP\Downloads\extracted\Hackathon_Ideal_Data.csv"")
Hackathon_Mapping_File = pd.read_csv(""C:\Users\HP\Downloads\extracted\Hackathon_Mapping_File.csv"")

# Displaying the first few rows of each dataset
print("Working Data:")
print(Hackathon_Working_Data.head())
print("\nValidation Data:")
print(Hackathon_Validation_Data.head())
print("\nIdeal Data:")
print(Hackathon_Ideal_Data.head())
print("\nMapping File:")
print(Hackathon_Mapping_File.head())

# Visualizing data
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Histogram for a column in Hackathon_Working_Data
axes[0, 0].hist(Hackathon_Working_Data['PRICE'], bins=20) 
axes[0, 0].set_title('Histogram of price')
axes[0, 0].set_xlabel('Values')
axes[0, 0].set_ylabel('Frequency')

# Scatter plot for a column in Hackathon_Validation_Data
axes[0, 1].scatter(Hackathon_Validation_Data['GRP'], Hackathon_Validation_Data['MONTH'], alpha=0.5)
axes[0, 1].set_title('Scatter Plot')
axes[0, 1].set_xlabel('X Axis Label')
axes[0, 1].set_ylabel('Y Axis Label')

# Bar plot for a column in Hackathon_Ideal_Data
axes[1, 0].bar(Hackathon_Ideal_Data['CMP'], Hackathon_Ideal_Data['VALUE']) 
axes[1, 0].set_title('Bar Plot')
axes[1, 0].set_xlabel('Category')
axes[1, 0].set_ylabel('Count')



plt.tight_layout()
plt.show()
