from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from models.training_model import training_model

def random_forest(df):
    X_train, X_test, y_train, y_test = training_model(df)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    # средна абсолютна грешка
    mae = mean_absolute_error(y_test, predictions)

    print(f"Random Forest - MAE (Mean Absolute Error): {round(mae, 2)}         lower is better")

    return y_test, predictions
