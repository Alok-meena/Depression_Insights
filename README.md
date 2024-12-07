# Depression_Insights

Depression Insights
This project leverages machine learning to analyze and predict depression based on psychological assessment scores (PHQ-9, GAD-7, Epworth Sleepiness Scale) and demographic attributes (age, gender, BMI). By combining multiple data points, it aims to support early detection and provide actionable insights for mental health care.



Features

1). Predicts depression likelihood with high accuracy using advanced ML models.

2). Integrates psychological scores and demographic data for a comprehensive analysis.

3). Visualizes insights with feature importance charts and AUC-ROC curves.

4). Provides explainable predictions to assist healthcare professionals.

Technologies Used

1). Languages: Python

2). Libraries: Scikit-learn, Pandas, Matplotlib, Seaborn

3). Algorithms: Logistic Regression, Random Forest, Gradient Boosting


Future Enhancements

1). Real-time data collection integration (e.g., wearables).

2). Expanding datasets to include diverse populations.

3). Extending the methodology to other mental health conditions.








How to Run

1).Clone the repository:


git clone https://github.com/yourusername/Depression_Insights.git

cd Depression_Insights


2). Install required dependencies:


pip install -r requirements.txt


3). Run the Streamlit app:

streamlit run app.py

4). Open the provided URL in your browser to access the app.



Evaluation Metrics and Results

1) Logistic regression:
• Accuracy: 0.82
• Precision: 0.60
• Recall: 0.94
• F1 score: 0.73

• Confusion matrix:

Actual/Predicted Positive Negative
  Positive          432     128
  Negative          13      192

  
2) Decision Tree:
• Accuracy: 0.88
• Precision: 0.76
• Recall: 0.81
• F1 score: 0.78


• Confusion matrix:

  Actual/Predicted Positive Negative
      Positive        508     52
      Negative         39     166

      
3) Random Forest:
• Accuracy: 0.88
• Precision: 0.76
• Recall: 0.81
• F1 score: 0.78


• Confusion matrix:


Actual/Predicted Positive Negative
    Positive         508    52
    Negative         39    166

    
4) Na¨ıve Bayes:
• Accuracy: 0.85
• Precision: 0.65
• Recall: 0.96
• F1 score: 0.77


• Confusion matrix:


Actual/Predicted Positive Negative
    Positive        455    105
    Negative         9     196
5) Neural Network:
• Accuracy: 0.88
• Precision: 0.76
• Recall: 0.82
• F1 score: 0.79


• Confusion matrix:

Actual/Predicted Positive Negative
     Positive       507    53
     Negative       37     168
