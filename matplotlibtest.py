import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'GlobalWeatherRepository.csv'

# Load the datasets
spain_df = pd.read_csv('Spain.csv')
brazil_df = pd.read_csv('Indonesia.csv')
indonesia_df = pd.read_csv('Brazil.csv')

# Convert the 'last_updated' column to datetime for each dataset
spain_df['last_updated'] = pd.to_datetime(spain_df['last_updated'])
brazil_df['last_updated'] = pd.to_datetime(brazil_df['last_updated'])
indonesia_df['last_updated'] = pd.to_datetime(indonesia_df['last_updated'])

# Find the min and max dates for each country
time_ranges = {
    'Country': ['Spain', 'Brazil', 'Indonesia'],
    'Start Date': [
        spain_df['last_updated'].min(),
        brazil_df['last_updated'].min(),
        indonesia_df['last_updated'].min()
    ],
    'End Date': [
        spain_df['last_updated'].max(),
        brazil_df['last_updated'].max(),
        indonesia_df['last_updated'].max()
    ]
}

# Create a DataFrame for visualization
time_ranges_df = pd.DataFrame(time_ranges)

# Plot temperature over time for a country
plt.figure(figsize=(12, 6))
plt.plot(spain_df['last_updated'], brazil_df['temperature_celsius'], label='Temperature (°C)', color='red')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time in Brazil')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()