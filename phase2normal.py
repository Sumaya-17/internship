import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
daily_data = pd.read_csv('C:\\Users\\HP\\Downloads\\climate\\daily_data.csv')
hourly_data = pd.read_csv('C:\\Users\\HP\\Downloads\\climate\\hourly_data.csv')
monthly_data = pd.read_csv('C:\\Users\\HP\\Downloads\\climate\\monthly_data.csv')
three_hour_data = pd.read_csv('C:\\Users\\HP\\Downloads\\climate\\three_hour_data.csv')

# Scatter plot for daily_data.csv
plt.figure(figsize=(10, 6))
plt.scatter(daily_data['DailyAverageDewPointTemperature'], daily_data['DailyAverageSeaLevelPressure'], color='blue')
plt.xlabel('Date')
plt.ylabel('DailyAverageSeaLevelPressure (°C)')
plt.title('Daily Temperature Variation')
plt.grid(True)
plt.show()

# Bar chart for monthly_data.csv
plt.figure(figsize=(10, 6))
monthly_mean_temperatures = monthly_data.groupby('MonthlySeaLevelPressure')['MonthlyDepartureFromNormalAverageTemperature'].mean()
monthly_mean_temperatures.plot(kind='bar', color='orange')
plt.xlabel('sealevel pressure over a month')
plt.ylabel('Average Monthly Mean Temperature (°F)')
plt.title('Average Monthly Mean Temperature')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Histogram for three_hour_data.csv
plt.figure(figsize=(10, 6))
plt.hist(three_hour_data['HourlyWindDirection'], bins=20, color='red', edgecolor='black')
plt.xlabel('wind direction')
plt.ylabel('Frequency')
plt.title('Temperature Distribution (Three-Hourly)')
plt.grid(True)
plt.show()  

# Convert 'HourlyDryBulbTemperature' column to numeric
hourly_data['HourlyDryBulbTemperature'] = pd.to_numeric(hourly_data['HourlyDryBulbTemperature'], errors='coerce')

# Drop rows with NaN values in 'HourlyDryBulbTemperature' column
hourly_data = hourly_data.dropna(subset=['HourlyDryBulbTemperature'])

# Define temperature ranges and labels for the pie chart
labels = ['Below 0°C', '0-10°C', '10-20°C', '20-30°C', 'Above 30°C']
bins = [-float('inf'), 0, 10, 20, 30, float('inf')]

# Bin the temperatures and count occurrences in each bin
temperature_bins = pd.cut(hourly_data['HourlyDryBulbTemperature'], bins=bins, include_lowest=True)
sizes = temperature_bins.value_counts(sort=False)

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'orange', 'gold', 'lightcoral'])
plt.title('Temperature Distribution (Hourly)')
plt.show()

