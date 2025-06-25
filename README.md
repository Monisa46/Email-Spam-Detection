Email Spam Detection

Welcome to the Email Spam Detection Project — a smart and interactive Streamlit app that classifies emails as Spam or Ham using Machine Learning. Built to enhance email safety, productivity, and awareness against cyber threats.

Features

- Cleans and preprocesses raw email text  
- Converts text into numerical form using TF-IDF  
- Trained with both Naive Bayes and SVM for model comparison  
- Displays key performance metrics: Accuracy, Precision, and Recall  
- Simple and interactive Streamlit interface

Dataset

Kaggle Spam Dataset: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset  
Over 5,000 labeled SMS/email messages marked as spam or ham  
Preprocessing includes:
- Lowercasing
- Stopword removal
- Tokenization
- TF-IDF vectorization

Built With

Python 3.10+  
Streamlit  
Pandas, NumPy  
Scikit-learn  
NLTK

Model Performance Comparison

| Metric     | Naive Bayes | SVM           |
|------------|-------------|---------------|
| Accuracy   | 96.59%      | 97.57%        |
| Precision  | 100%        | 97.67%        |
| Recall     | 74.66%      | 84.00%        |

Conclusion:  
Naive Bayes offers high precision (great for avoiding false positives) but lower recall.  
SVM provides better overall balance and higher accuracy, making it more suitable for production use.





youtube link with voice over :https://youtu.be/LoNC3G75su8

License

This project is licensed under the MIT License — free to use, modify, and share with attribution.

About the Creator

Created by Monisa R, a CSBS student passionate about combining business systems and machine learning to solve real-world problems.

LinkedIn: https://www.linkedin.com/in/monisa-r-17a41228b/  
Email: monisa4606@gmail.com


