from google.colab import drive
import pandas as pd
from IPython.display import display
from scipy import stats

# Mount Google Drive
drive.mount('/content/drive')

# Load the dataset from the specified path
file_path = '/content/drive/MyDrive/{yourfilepath}'
df = pd.read_csv(file_path)
# print(df)

# Select relevant columns for descriptive statistics
data = df[["SUS of Effect", "Likert mean of Effect", "Number of Clicks", "Total duration of mouse hover links"]]

# Calculate descriptive statistics: mean, standard deviation, and median
descriptive_stats = {
    'Mean': data.mean(),
    'Standard Deviation': data.std(),
    'Median': data.median()
}

# Create a DataFrame to display the results
df_descriptive_stats = pd.DataFrame(descriptive_stats)

# Print the descriptive statistics
print(df_descriptive_stats)


# Group the data by "Effect" 
grouped_data = df.groupby("Effect(popup or highlight)")[["SUS of Effect", "Likert mean of Effect", "Number of Clicks", "Total duration of mouse hover links"]]

# Calculate mean, standard deviation, and median for each group
grouped_stats = grouped_data.agg(['mean', 'std', 'median'])


# Remove the gradient and display the table normally
styled_stats = grouped_stats.style.set_caption("Grouped Descriptive Statistics by Effect")


# Display the styled DataFrame
display(styled_stats)


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


# Remove the gradient and display the table normally
styled_stats = df_t_test_results.style.set_caption("Grouped Descriptive Statistics by Effect")


# Display the t-test results
display(styled_stats)

