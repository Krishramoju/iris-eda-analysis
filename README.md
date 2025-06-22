# Iris Dataset Analysis

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/krishramoju/iris-eda-analysid/blob/main/iris_eda.ipynb)


Complete EDA performed directly on GitHub:

1. **Data Loading**: Loaded iris.csv
2. **Statistics**:
   - Calculated mean, median, standard deviation
   - Generated full .describe() output
3. **Visualization**: Histograms for all features

## Sample Code
```python
import pandas as pd
df = pd.read_csv('iris.csv')
df.describe()
```

## How to View Results
GitHub will show static outputs. For full interactive view:
1. Click the nbviewer badge above
2. Or download and run locally with Jupyter
