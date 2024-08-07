import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

train_data = pd.read_csv('week7/train.csv')

for column in train_data.columns:
    if train_data[column].dtype == 'object':
        train_data[column].fillna(train_data[column].mode()[0], inplace=True)
    else:
        train_data[column].fillna(train_data[column].median(), inplace=True)

train_data = pd.get_dummies(train_data)

X = train_data.drop(['Id', 'SalePrice'], axis=1)
y = train_data['SalePrice']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_val)
rmse = np.sqrt(mean_squared_error(np.log(y_val), np.log(y_pred)))
print(f'Validation RMSE: {rmse}')

r2 = r2_score(y_val, y_pred)
print(f'R-squared: {r2:.4f}')

test_data = pd.read_csv('week7/test.csv')

test_ids = test_data['Id']

for column in test_data.columns:
    if test_data[column].dtype == 'object':
        test_data[column].fillna(test_data[column].mode()[0], inplace=True)
    else:
        test_data[column].fillna(test_data[column].median(), inplace=True)

test_data = pd.get_dummies(test_data)

missing_cols = set(X.columns) - set(test_data.columns)
for col in missing_cols:
    test_data[col] = 0
test_data = test_data[X.columns]

test_data['Id'] = test_ids

test_preds = model.predict(test_data.drop('Id', axis=1))

submission = pd.DataFrame({'Id': test_data['Id'], 'SalePrice': test_preds})

submission.to_csv('week7/submission.csv', index=False)
