# Invoice Fraud Detection

Detects fraudulent invoices using machine learning on synthetic 
enterprise invoice data modelling real-world fraud patterns.

## Tech Stack
Python, pandas, scikit-learn, matplotlib, Faker, Jupyter Notebook

## Approach
- Generated 2000 synthetic invoices with 8% fraud rate using Faker
- Engineered fraud signals: payment speed, amount anomaly, duplicate flag
- Trained Random Forest classifier (100 estimators)
- Evaluated with precision/recall/confusion matrix

## Results
- days_to_pay and amount are top fraud signals (feature importance)
- High recall on fraud class — minimises missed fraud cases

## Status
In Progress — EDA and baseline model complete.
Next: XGBoost comparison, SHAP explainability

## Run It
pip install -r requirements.txt
python data/generate_data.py
jupyter notebook notebook.ipynb