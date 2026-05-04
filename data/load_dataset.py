import pandas as pd
pd.set_option('display.max_columns', None)

def get_dataset():
    return pd.read_csv("data/CPU_benchmark_v4.csv")



def load_dataset():
    df = get_dataset()

    get_numeric_columns = df.select_dtypes(include=['int64', 'float64'])
    print(get_numeric_columns.drop(columns=['testDate']).describe())









