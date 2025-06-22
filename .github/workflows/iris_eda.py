import pandas as pd
import matplotlib.pyplot as plt

# Load data from URL
url = 'https://bit.ly/4nejNue'
df = pd.read_csv(url)

# Show basic stats
print("Basic Stats:\n", df.describe())

# Mean, Median, Std
print("\nMeans:\n", df.mean(numeric_only=True))
print("\nMedians:\n", df.median(numeric_only=True))
print("\nStandard Deviations:\n", df.std(numeric_only=True))

# Save histograms as an image
df.hist(figsize=(10, 8), bins=15)
plt.tight_layout()
plt.savefig("iris_histograms.png")
print("\nHistograms saved as 'iris_histograms.png'.")

# Group by species (bonus)
print("\nGrouped Stats by Species:\n", df.groupby('species').describe())
