import pandas as pd
from models.linear_regression_model import linear_regression
from models.random_forest_model import random_forest
from data.data_preprocessing import clean_data

def create_comparison_table():
    df = clean_data()

    y_test_lr, predictions_lr = linear_regression(df)
    y_test_rf, predictions_rf = random_forest(df)

    #create new dataframe table
    comparison_table = pd.DataFrame({
        "Real_cpuMark": y_test_lr.values,

        "Linear_R_Predicted": predictions_lr.round(2),
        "Linear_R_Error": abs(y_test_lr - predictions_lr).round(2),

        "Random_F_Predicted": predictions_rf.round(2),
        "Random_F_Error": abs(y_test_rf - predictions_rf).round(2)
    })

    print("\nComparison Table of real and predicted values:")
    print(comparison_table.head(10).to_string(index=False))