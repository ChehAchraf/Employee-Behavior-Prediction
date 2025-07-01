# Employee Behavior Prediction

This project uses logistic regression to predict the behavior of employees based on their grades, absence, and issues. The main script is `1.py`.

## Features
- Encodes employee behavior as numeric labels.
- Trains a logistic regression model to predict behavior.
- Predicts the behavior of a new employee based on input features.
- Uses a small, sample dataset (see `employers_data.csv`).

## Files
- `1.py`: Main script for training and prediction.
- `employers_data.csv`: Example dataset of employees and their features.
- `data.csv`: (Not used by the main script, can be ignored.)

## Requirements
- Python 3.x
- pandas
- numpy
- scikit-learn
- matplotlib (imported, but not used)

Install dependencies with:
```bash
pip install pandas numpy scikit-learn matplotlib
```

## Usage
Run the script with:
```bash
python 1.py
```

This will output the predicted behavior for a new employee with the following features:
- grades_logic: 60
- grades_open: 50
- grades_help: 60
- absence: 3
- issues: 3

## Output Example
```
the beahvior of the new student is : bad
```

## Notes
- The script uses a hardcoded dataset, but you can uncomment the line in the script to export it as `employers_data.csv`.
- The model uses logistic regression to classify behavior into categories such as 'good', 'bad', 'average', and 'excellent'. 
