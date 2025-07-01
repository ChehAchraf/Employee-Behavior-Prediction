Employee Behavior Prediction
Overview
This project uses a logistic regression model to predict employee behavior based on various features such as logic grades, openness grades, helpfulness grades, absence count, and reported issues. The dataset includes information about employees and their respective attributes, which are used to train the model.
Features

grades_logic: Scores representing logical reasoning ability (0-100).
grades_open: Scores representing openness (0-100).
grades_help: Scores representing helpfulness (0-100).
absence: Number of absences.
issues: Number of reported issues.
behavior: Categorical target variable (good, bad, average, excellent) encoded numerically for modeling.

Dependencies

Python 3.x
pandas
numpy
matplotlib
scikit-learn

Install the dependencies using:
pip install pandas numpy matplotlib scikit-learn

Dataset
The dataset is created within the script and includes:

Employee names
Grades for logic, openness, and helpfulness
Absence count
Reported issues
Behavior labels (good, bad, average, excellent)

The data is stored in a pandas DataFrame for processing.
Usage

Data Preparation:

The dataset is loaded into a pandas DataFrame.
The behavior column is encoded into numerical values using LabelEncoder.
Features (grades_logic, grades_open, grades_help, absence, issues) are separated from the target variable (behavior_Numeric).


Model Training:

The data is split into training (80%) and testing (20%) sets using train_test_split.
A logistic regression model (LogisticRegression) is trained on the training data with a maximum of 1000 iterations.


Prediction:

The model predicts the behavior of a new employee based on input features.
The prediction is converted back to the original categorical label (e.g., good, bad, average, excellent) using the inverse transform of LabelEncoder.


Example:
new_employers = {
    'grades_logic': 60,
    'grades_open': 50,
    'grades_help': 60,
    'absence': 3,
    'issues': 3
}
new_employers = pd.DataFrame([new_employers])
new_employers_predetc = model.predict(new_employers)
convert = le.inverse_transform(new_employers_predetc)
print(f'the behavior of the new employee is: {convert[0]}')



How to Run

Ensure all dependencies are installed.
Copy the provided Python script into a .py file (e.g., employee_behavior.py).
Run the script:python employee_behavior.py


The script will output the predicted behavior for the new employee based on the provided input features.

Notes

The dataset is small and synthetic. For real-world applications, a larger and more diverse dataset is recommended.
The model assumes linear relationships between features and the target variable. For more complex relationships, consider other models like decision trees or neural networks.
The commented-out line # df.to_csv('employers_data.csv', index=False) can be used to save the dataset to a CSV file for further analysis.

License
This project is unlicensed and free to use for educational purposes.
