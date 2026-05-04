import matplotlib.pyplot as plt
import seaborn as sns
from data.load_dataset import get_dataset


def histogram():
    df = get_dataset()
    df['cpuMark'].hist(bins=30)
    plt.title('Разпределение на CPU производителност (cpuMark)')
    plt.xlabel('Производителност на процесора (cpuMark)')
    plt.ylabel('Честота на срещане (Frequency)')
    plt.show()


def boxplot():
    df = get_dataset()
    plt.boxplot(df['cpuMark'])
    plt.title('Бок графика на производителността на процесорите (cpuMark)')
    plt.ylabel('Производителност (cpuMark)')
    plt.xlabel('Процесори (CPU)')
    plt.show()

def scatterplot():
    df = get_dataset()
    plt.scatter(df['price'], df['cpuMark'])
    plt.title('Зависимост между цена и производителност на процесорите')
    plt.xlabel('Цена (Price)')
    plt.ylabel('Производителност (cpuMark)')
    plt.show()

def corelation_matrix():
    df = get_dataset()
    # get only number values
    df_numeric = df.select_dtypes(include='number')
    # remove testDate column
    df_numeric = df_numeric.drop(columns=['testDate'])
    # Calculate correlation
    corr_matrix = df_numeric.corr()
    # round decimal point
    corr_matrix = round(corr_matrix , 2)
    print(corr_matrix)

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix,
        annot=True,
        cmap=sns.diverging_palette(950, 150, n=500),
        center=0,
        linewidths=0.5
    )

    plt.title('Корелационна матрица (Heatmap)')
    plt.show()




def intel_vs_amd_performance():
    df = get_dataset()

    brands = []
    for name in df['cpuName']:
        if 'Intel' in name:
            brands.append('Intel')
        elif 'AMD' in name:
            brands.append('AMD')
        else:
            brands.append('Other')

    df['brand'] = brands
    #get only brand Intel and AMD
    df_filtered = df[df['brand'].isin(['Intel', 'AMD'])]
    #remove price NanN, if any
    df_filtered = df_filtered.dropna(subset=['price'])

    #group by brand and calculate mean for every group
    avg_price = df_filtered.groupby('brand')['price'].mean()

    brandsCPU = avg_price.index
    prices = avg_price.values

    plt.bar(brandsCPU, prices)
    #price over columns
    for i in range(len(prices)):
        plt.text(i, prices[i], f"{prices[i]:.0f}", ha='center')
    plt.title('Сравнение на средна цена между Intel vs AMD')
    plt.xlabel('Производител (Brand)')
    plt.ylabel('Средна цена (Average price)')
    plt.show()


