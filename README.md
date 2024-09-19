
# Within-Group Experiment Data Analysis in Google Colab

## Overview
This project is a simple statistical analysis of a COMPSCI705 within-group experiment using a dataset stored in a CSV file. The experiment involves comparing two effects (popup window vs. highlight) across several variables, including SUS score, Likert score, Number of Clicks, and Total duration of mouse hover links. To find out what was different between the two situations, we used descriptive statistics and a paired t-test.
- **SUS Score**
- **Likert Score**
- **Number of Clicks**
- **Total Duration of Mouse Hover Links**

We perform **descriptive statistics** and a **paired t-test** to analyze differences between the two conditions.

## Running Environment: Google Colab
The entire process runs in **Google Colab**. You'll load the dataset from Google Drive and use Python libraries (`pandas`, `scipy`) for data analysis, displaying the results interactively.

My code can be found in Google Collab at this link: https://colab.research.google.com/drive/1LbjnndCma6FKCiaX4pGza3XauR2px5Vj?usp=sharing

## Requirements
- **Google Colab** account
- CSV dataset

## Steps to Run the Project

### 1. Link Your Google Drive
The dataset is stored in Google Drive, so you must link your drive before loading the file:
![image](https://github.com/user-attachments/assets/e84c5f37-aabf-455c-b263-7305a7ec29fa)

```python
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')
```

### 2. Load the Dataset
Replace `'{yourfilepath}'` with the actual path of your CSV file in Google Drive.

```python
import pandas as pd

# Load the dataset from the specified path
file_path = '/content/drive/MyDrive/{yourfilepath}'
df = pd.read_csv(file_path)

# Optional: View the first few rows
print(df.head())
```

### 3. Descriptive Statistics
To calculate **mean**, **standard deviation**, and **median** for the variables (SUS score, Likert score, etc.):

```python
# Select relevant columns for descriptive statistics
data = df[["SUS of Effect", "Likert mean of Effect", "Number of Clicks", "Total duration of mouse hover links"]]

# Calculate descriptive statistics
descriptive_stats = {
    'Mean': data.mean(),
    'Standard Deviation': data.std(),
    'Median': data.median()
}

# Create a DataFrame to display the results
df_descriptive_stats = pd.DataFrame(descriptive_stats)

# Print the descriptive statistics
print(df_descriptive_stats)
```

### 4. Grouped Descriptive Statistics by Effect
Perform grouped descriptive statistics based on the **Effect** (popup or highlight):

```python
# Group the data by "Effect"
grouped_data = df.groupby("Effect(popup or highlight)")[["SUS of Effect", "Likert mean of Effect", "Number of Clicks", "Total duration of mouse hover links"]]

# Calculate mean, standard deviation, and median for each group
grouped_stats = grouped_data.agg(['mean', 'std', 'median'])

# Display the styled DataFrame
from IPython.display import display
styled_stats = grouped_stats.style.set_caption("Grouped Descriptive Statistics by Effect")
display(styled_stats)
```

### 5. Paired T-Test (Within-Group Test)
To perform a **paired t-test** comparing **popup** and **highlight** effects for each variable:

```python
from scipy import stats

# Separate the data based on "Effect" (popup vs highlight)
popup_group = df[df["Effect(popup or highlight)"] == "popup"]
highlight_group = df[df["Effect(popup or highlight)"] == "highlight"]

# Perform paired t-tests for each relevant column
t_test_results = {
    'SUS of Effect': stats.ttest_rel(popup_group["SUS of Effect"], highlight_group["SUS of Effect"]),
    'Likert mean of Effect': stats.ttest_rel(popup_group["Likert mean of Effect"], highlight_group["Likert mean of Effect"]),
    'Number of Clicks': stats.ttest_rel(popup_group["Number of Clicks"], highlight_group["Number of Clicks"]),
    'Total duration of mouse hover links': stats.ttest_rel(popup_group["Total duration of mouse hover links"], highlight_group["Total duration of mouse hover links"])
}

# Convert the t-test results to a DataFrame for easier visualization
df_t_test_results = pd.DataFrame(t_test_results, index=['t-statistic', 'p-value'])

# Display the t-test results
styled_ttest = df_t_test_results.style.set_caption("Paired T-Test Results")
display(styled_ttest)
```
