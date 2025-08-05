<!-- # Elastic-Net-Regression

<img width="1813" height="918" alt="image" src="https://github.com/user-attachments/assets/a6298c43-503b-4a85-bf72-2f61b97b6dbb" /> -->


## Insurance Charge Predictor – Elastic Net Regression

This project uses Elastic Net Regression, a hybrid of Lasso and Ridge regression, to predict medical insurance charges based on user details like age, BMI, smoking status, etc. It features a simple and clean Flask web app to gather user inputs and return predictions.

---

## Why Elastic Net?
- Elastic Net Regression combines the strengths of both Lasso (L1) and Ridge (L2) regularization. It is particularly useful when:

- There are multiple correlated features.

- You want to perform feature selection (like Lasso) while still maintaining model stability (like Ridge).

---

##  Project Structure
```
Elastic-Net-Regression/
├── app.py                   # Flask application for prediction
├── train_model.py           # Model training using Elastic Net
├── model.pkl                # Trained model
├── encoders.pkl             # Encoded mappings for categorical fields
├── insurance_data.csv       # Dataset used for training
│
├── templates/
│   └── index.html           # Frontend form UI
└── static/
    └── style.css            # Optional styling file

```
---

##  Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/Digvijay4252/Elastic-Net-Regression.git
cd Elastic-Net-Regression
```
Install dependencies
```
pip install -r requirements.txt
```
Run the application
```
python app.py
```
Open in browser

Visit: http://localhost:5000

# Sample Input
```
Age: 45
BMI: 27.5
Smoker: Yes
Children: 2
Region: Southeast
```

## Screenshots
<img width="1813" height="918" alt="image" src="https://github.com/user-attachments/assets/a6298c43-503b-4a85-bf72-2f61b97b6dbb" />

## Future Improvements
Add visualization for feature contributions

Include confidence interval with predictions

Export prediction history

Deploy to Heroku, Render, or Docker