from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from models.training_model import training_model

def linear_regression(df):
    X_train, X_test, y_train, y_test = training_model(df)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    print(f"Linear Regression - MAE (Mean Absolute Error): {round(mae, 2)}     lower is better")

    return y_test, predictions

