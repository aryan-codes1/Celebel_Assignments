import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Read the CSV file
df = pd.read_csv('train.csv')

# Dropping columns which are not useful
cols = ['Name', 'Ticket', 'Cabin']
df = df.drop(cols, axis=1)

# Dropping rows having missing values
df = df.dropna()

# Create dummy variables for categorical columns
dummies = []
cols = ['Pclass', 'Sex', 'Embarked']
for col in cols:
    dummies.append(pd.get_dummies(df[col]))
titanic_dummies = pd.concat(dummies, axis=1)
df = pd.concat((df, titanic_dummies), axis=1)

# Drop the original categorical columns
df = df.drop(['Pclass', 'Sex', 'Embarked'], axis=1)

# Interpolate missing values in the 'Age' column
df['Age'] = df['Age'].interpolate()

# Prepare the input features and target variable
X = df.drop('Survived', axis=1).values
y = df['Survived'].values

# Remove the second column from the input features
X = np.delete(X, 1, axis=1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Standardize the input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
