import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load datasets
math_data = pd.read_csv('Final_Project/student/student-mat.csv', sep=';')
por_data = pd.read_csv('Final_Project/student/student-por.csv', sep=';')

# Merge datasets on common attributes to avoid duplication
common_columns = list(set(math_data.columns).intersection(set(por_data.columns)))
merged_data = pd.merge(math_data, por_data, on=common_columns, how='outer')

# Preprocessing
# Convert categorical variables to dummy variables
merged_data = pd.get_dummies(merged_data)

# Assuming 'G3' is the target variable for both datasets
X = merged_data.drop('G3', axis=1)
y = merged_data['G3']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model creation
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Predictions
y_pred = model.predict(X_test_scaled)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Plotting actual vs predicted values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Grades')
plt.ylabel('Predicted Grades')
plt.title('Actual vs Predicted Grades')
plt.show()

# Assuming y_test and y_pred are already defined as shown in your code

# Generate a range of numbers equal to the length of y_test to serve as student identifiers
student_ids = range(len(y_test))

# Plotting student identifiers vs predicted grades
plt.figure(figsize=(12, 6))
plt.scatter(student_ids, y_test, color='blue', label='Actual Grades')
plt.scatter(student_ids, y_pred, color='red', label='Predicted Grades', alpha=0.5)
plt.title('Comparison of Actual and Predicted Grades by Student')
plt.xlabel('Student Identifier')
plt.ylabel('Grades')
plt.legend()
plt.show()

# Assuming a threshold of difference, e.g., students who got predicted grades 2 points lower than actual grades need help
threshold = 2

# Identifying students requiring help based on the threshold
students_requiring_help = [(actual, predicted, student_id) for actual, predicted, student_id in zip(y_test, y_pred, student_ids) if actual - predicted >= threshold]
print(students_requiring_help)
# Now, students_requiring_help contains tuples of (actual_grade, predicted_grade, student_id) for each student requiring help