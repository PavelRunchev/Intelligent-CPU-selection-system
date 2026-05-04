from sklearn.model_selection import train_test_split


def training_model(df):
    X = df[['price', 'cores', 'TDP']]
    y = df['cpuMark']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


