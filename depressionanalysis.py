# -- coding: utf-8 --
"""DepressionAnalysis.ipynb"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score
import joblib
# from google.colab import files

# Load the dataset
data = pd.read_csv('college_student_health_data.csv')
print(data.sample(10))
print(data.info())
print(data.describe())

# Data Preprocessing
data['gender'] = data['gender'].map({'Male': 0, 'Female': 1})  # Convert gender to numeric
data['depressiveness'] = data['depressiveness'].astype(int)     # Ensure depressiveness is integer

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values:\n", missing_values)

# Drop rows with missing values
data = data.dropna()

# Split data into features (X) and target (Y)
X = data[['age', 'gender', 'study_year', 'bmi', 'phq_score', 'gad_7_score', 'epworth_score']]
Y = data['depressiveness']

# Define categorical and numerical features for transformation
categorical_features = ['gender', 'study_year']
numerical_features = ['age', 'bmi', 'phq_score', 'gad_7_score', 'epworth_score']

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_features)
    ])

# Combine the preprocessor and model into a pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', LogisticRegression(random_state=42))])

# Split data into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Fit the pipeline on the training data
pipeline.fit(X_train, Y_train)

# Predict on the test set
Y_pred = pipeline.predict(X_test)

# Evaluation metrics
accuracy = accuracy_score(Y_test, Y_pred)
precision = precision_score(Y_test, Y_pred)
recall = recall_score(Y_test, Y_pred)
f1 = f1_score(Y_test, Y_pred)
roc_auc = roc_auc_score(Y_test, pipeline.predict_proba(X_test)[:, 1])

# Confusion matrix
conf_matrix = confusion_matrix(Y_test, Y_pred)

# Display results
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")
print(f"ROC-AUC Score: {roc_auc:.2f}")
print(f"Confusion Matrix:\n{conf_matrix}")

# Load new test data and apply the same preprocessing steps
Tdata = pd.read_csv('college_student_health_data.csv')

# Check for missing values and drop them
missing_values = Tdata.isnull().sum()
print("Missing values in test data:\n", missing_values)
Tdata = Tdata.dropna()

# Select necessary columns and ensure column names are consistent with training data
Tdata = Tdata.rename(columns={'gad_score': 'gad_7_score', 'school_year': 'study_year'})
data_test = Tdata[['age', 'gender', 'study_year', 'bmi', 'phq_score', 'gad_7_score', 'epworth_score']]

# Convert gender in the new test data
data_test.loc[:, 'gender'] = data_test['gender'].map({'male': 0, 'female': 1})  # Using .loc to avoid SettingWithCopyWarning

# Extract target values for evaluation
data_y = Tdata['depressiveness'].astype(int)

# Use the pipeline to transform and predict on the new test data
Y_pred_2 = pipeline.predict(data_test)

# Evaluate the pipeline on the new test data
accuracy = accuracy_score(data_y, Y_pred_2)
print(f"Accuracy on new test data: {accuracy:.2f}")

# Save the pipeline to a file
joblib.dump(pipeline, 'decision_tree_pipeline_model_dt.pkl')

# Download the saved model
# files.download('model_pipeline.pkl')  # Uncomment this line if running in Colab to download the model