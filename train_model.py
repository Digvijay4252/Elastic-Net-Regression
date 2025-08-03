import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv('insurance_data.csv')

# Encode categorical columns
encoders = {}
for col in ['sex', 'smoker', 'region']:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoders[col] = le

# Features and target
X = data[['age', 'sex', 'bmi', 'children', 'smoker', 'region']]
y = data['charges']

# Train Elastic Net model
model = ElasticNet(alpha=1.0, l1_ratio=0.5)  # You can tune alpha and l1_ratio
model.fit(X, y)

# Save model and encoders
joblib.dump(model, 'model.pkl')
joblib.dump(encoders, 'encoders.pkl')

print("Elastic Net model and encoders saved successfully.")
