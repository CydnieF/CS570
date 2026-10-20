# Module 5 - Student Starter Code 

# This code is provided as a starting point for the assignment.
# You are expected to complete the code and implement the required functionality. 
# TODO: Import libraries for whatever you need to complete the assignment (the libraries below are for reference and are incomplete).
import numpy as np
import pandas as pd

# Import libraries for visualization from matplotlib and seaborn and inspection from sklearn
import matplotlib.pyplot as plt
import seaborn as sns

# TODO: Import libraries for preprocessing from sklearn

# Import libraries for imputation from sklearn
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer
from sklearn.impute import IterativeImputer

# Import libraries for model model selection and metrics from sklearn
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline

# Import libraries for regression from sklearn
from sklearn.linear_model import LinearRegression

# Function to test dataset on a linear regression model
# Use this function to compare how different imputation methods affect the model performance
def get_score(df, imputer=None): 

       # Define features (X) and target (y)
    X = df.drop(columns=["Class"])
    y = df["Class"]

    regressor = LinearRegression()
    if imputer is not None:
        estimator = make_pipeline(imputer, regressor)
    else:
        estimator = regressor
    scores = cross_val_score(
        estimator, X, y, scoring="neg_mean_squared_error", cv=4
    )
    return scores.mean(), scores.std()


#----------------------------------------------------------------
# Step 1: Load the CSV file into a pandas DataFrame
#----------------------------------------------------------------
df = pd.read_csv("Module5Dataset.csv")  

#----------------------------------------------------------------
# Step 2: Data Exploration and Visualization
#         Does the data contain NAN or nan values (implying incomplete data)?
#         What type of data is in the dataset?
#----------------------------------------------------------------

    # TODO: Display information about the dataset

    # TODO: Dispay the unique values in each feature

    # TODO: Visualize the distribution of 'Features'
plt.show()


#----------------------------------------------------------------
# Step 3: TODO: Does the dataset work on the linear regression model before preprocessing?
#         TODO: What type of data does the sklearn linear regression model accept?
#----------------------------------------------------------------

x_labels = []

mses = np.zeros(5)
stds = np.zeros(5)

mses[0], stds[0] = get_score(original dataset just after loading) # Does it work?
x_labels.append("RAW Dataset")

#----------------------------------------------------------------
# Step 4: TODO: Transform the dataset
#         Note: It is possible to impute missing values in the dataset before transforming it.
#               or even at the same time.
#----------------------------------------------------------------

#----------------------------------------------------------------
# Step 5: TODO: Impute missing values in the dataset (replace NAN or nan values)
#         Experiment with the following imputers: 
#         - SimpleImputer with strategy='constant' and fill_value=0
#         - SimpleImputer with strategy='mean'
#         - KNNImputer
#         - IterativeImputer
#----------------------------------------------------------------

# Example code for documentation only
imputer = SimpleImputer(strategy="constant", fill_value=0)
mses[1], stds[1] = get_score(???????????, imputer)
x_labels.append("Zero Imputation")

imputer = SimpleImputer(strategy="mean")
mses[2], stds[2] = get_score(??????????????, imputer)
x_labels.append("Mean Imputation")

imputer = KNNImputer()
mses[3], stds[3] = get_score(??????????/, imputer)
x_labels.append("KNN Imputation")

imputer = IterativeImputer(max_iter=10, random_state=42)
mses[4], stds[4] = get_score(??????????????/, imputer)
x_labels.append("Iterative Imputation")


#----------------------------------------------------------------
# Step 6: TODO: Collect data metrics and visualization of:
#         Dataset after transforming
#         Dataset after imputing missing values
#         sns.heatmap(?????????.corr(), annot=True, cmap="coolwarm", fmt=".2f")
#--------------------------------------------------------------------

print("Negative Mean Squared Errors (MSEs):", mses)
print("Standard Deviations (STDs):", stds)

# Plot the results
plt.figure(figsize=(10, 6))
plt.bar(x_labels, stds, yerr=stds, capsize=5)
plt.xlabel("Imputation Method")
plt.ylabel("Negative Mean Squared Error")
plt.title("Comparison of Imputation Methods")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
