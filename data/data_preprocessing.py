from data.load_dataset import get_dataset

# помощна функция за добавяне на колона brand
def extract_brand(cpu_name):
    if not isinstance(cpu_name, str) or cpu_name.strip() == '':
        return 'Unknown'
    return cpu_name.split()[0]

# # функция за почистване на данните
def clean_data():
    df = get_dataset()

    # remove None values
    df = df.dropna(subset=['price', 'socket', 'TDP'])

    # remove duplicate values
    df = df.drop_duplicates(subset=['cpuName'])

    # remove unknown values
    df = df[df['socket'] != 'unknown']
    df = df[df['category'] != 'Unknown']

    # remove column testDate
    df = df.drop(columns=['testDate'], errors='ignore')

    # add new column brand
    df['brand'] = df['cpuName'].apply(extract_brand)
    df = df[df['brand'] != 'Unknown']

    #converting price from dollar to euro
    df['price'] = (df['price'] * 0.92).round(2)

    return df.reset_index(drop=True)


def get_top_cpus(n=100):
    df = clean_data()
    return df.sort_values(by='cpuMark', ascending=False).head(n)


def process_missing_values():
    df = get_dataset()
    # Проверка за липсващи стойности
    print("Липсващи стойности по колони:")
    print(df.isnull().sum())

    # Попълване на числови стойности със средна стойност
    df['price'] = df['price'].fillna(df['price'].mean())
    df['cpuValue'] = df['cpuValue'].fillna(df['cpuValue'].mean())
    df['threadValue'] = df['threadValue'].fillna(df['threadValue'].mean())
    df['TDP'] = df['TDP'].fillna(df['TDP'].mean())

    # Попълване на категорийни стойности с най-често срещаната стойност (mode)
    df['socket'] = df['socket'].fillna(df['socket'].mode()[0])
    df['category'] = df['category'].fillna(df['category'].mode()[0])

    return df

