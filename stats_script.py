import polars as pl
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load the dataset
df = pl.read_csv('camera_dataset.csv')

# Calculate descriptive statistics
descriptive_stats = df.select([
    pl.col('Price').mean().alias('mean_price'),
    pl.col('Price').median().alias('median_price'),
    pl.col('Price').std().alias('std_dev_price')
]).to_pandas()

# Print the statistics to console
print(descriptive_stats)

# Generate a histogram of the 'Price' column
plt.figure()
histogram = df['Price'].to_pandas().hist(bins=30)
plt.title('Histogram of Camera Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.savefig('price_histogram.png')  # save the histogram to a file
plt.close()

# Save the descriptive statistics to a CSV file
descriptive_stats.to_csv('descriptive_stats.csv')

# Function to generate PDF using reportlab
def generate_pdf(stats):
    c = canvas.Canvas("summary_report.pdf", pagesize=letter)
    width, height = letter
    c.drawString(72, height - 72, "Summary Report: Camera Prices")
    c.drawString(72, height - 100, f"Mean Price: {stats['mean_price'][0]}")
    c.drawString(72, height - 120, f"Median Price: {stats['median_price'][0]}")
    c.drawString(72, height - 140, f"Standard Deviation: {stats['std_dev_price'][0]}")
    
    c.drawString(72, height - 180, "See 'price_histogram.png' for the visual representation.")
    c.save()

# Call the function to generate PDF
generate_pdf(descriptive_stats)
