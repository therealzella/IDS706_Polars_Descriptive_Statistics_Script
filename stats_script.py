import polars as pl
import matplotlib.pyplot as plt

# Load the dataset
df = pl.read_csv('camera_dataset.csv')  

# Calculate descriptive statistics
descriptive_stats = df.select([
    pl.col('Price').mean().alias('mean_price'),
    pl.col('Price').median().alias('median_price'),
    pl.col('Price').std().alias('std_dev_price')
])

# Print the statistics
print(descriptive_stats)

# Generate a histogram of the 'Price' column
plt.figure()
df['Price'].to_pandas().hist(bins=30)
plt.title('Histogram of Camera Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.savefig('price_histogram.png')  # save the histogram to a file
plt.close()

# Save the descriptive statistics to a CSV file
descriptive_stats.to_pandas().to_csv('descriptive_stats.csv')
