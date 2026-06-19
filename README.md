# Invoice Fraud Detection — ML Classifier

**Status:** Machine Learning Project | End-to-End ML Pipeline | Synthetic Enterprise Dataset

A machine learning project that detects potentially fraudulent invoices using a Random Forest classifier trained on synthetic invoice data. This project explores an end-to-end machine learning workflow, including data generation, feature engineering, model training, evaluation, and visualization.

## Why I Built This

Invoice fraud, such as duplicate submissions, unusual payment timings, and suspicious invoice amounts, is a common challenge in enterprise finance systems. I built this project to gain hands-on experience in applying machine learning to a realistic business problem and to understand the fundamentals of fraud detection systems.

## Approach

### Synthetic Data Generation

* Generated 2,000 synthetic invoice records using Faker.
* Introduced an 8% fraud rate to create a realistic class imbalance.
* Simulated fraud scenarios such as duplicate invoices, unusually small or large amounts, and suspiciously fast payments.

### Feature Engineering

Created features that may indicate fraudulent behaviour:

* Invoice amount
* Days taken for payment
* Number of items in an invoice
* Weekend submission indicator
* Duplicate invoice flag

### Exploratory Data Analysis (EDA)

* Visualized invoice amount distributions and fraud patterns.
* Examined the relationship between fraud and weekend submissions.

### Model Training

* Split the data into training and testing sets.
* Trained a Random Forest classifier with 100 estimators.
* Evaluated the model using classification metrics and a confusion matrix.

### Feature Importance

* Analysed which features contributed most to fraud prediction.
* In this dataset, payment timing and invoice amount emerged as some of the strongest indicators of fraud.

## Tech Stack

* Python
* pandas
* scikit-learn
* matplotlib
* Faker
* Jupyter Notebook

## Project Structure

```text
invoice-fraud-detection/
├── data/
│   ├── generate_data.py
│   └── invoices.csv
├── notebook.ipynb
├── eda_plot.png
├── feature_importance.png
├── confusion_matrix.png
├── requirements.txt
└── README.md
```

## Run It Locally

```bash
# Clone the repository
git clone https://github.com/ManikandanPrabhu13/invoice-fraud-detection.git

# Move into the project directory
cd invoice-fraud-detection

# Install dependencies
pip install -r requirements.txt

# Generate the synthetic dataset
python data/generate_data.py

# Launch Jupyter Notebook
jupyter notebook
```

## Future Improvements

* Compare the Random Forest model with Logistic Regression and XGBoost baselines.
* Add explainability techniques such as SHAP values.
* Experiment with larger and more diverse synthetic datasets.
* Build a simple dashboard to visualize fraud predictions and model insights.

## Learning Outcome

This project helped me gain practical experience in building an end-to-end machine learning pipeline and applying machine learning techniques to a realistic business problem. It also improved my understanding of feature engineering, class imbalance, model evaluation, and interpreting results in a business context.

## Author

**Manikandan Prabhu B**
Electronics and Communication Engineering (ECE) Student
GitHub: https://github.com/ManikandanPrabhu13
