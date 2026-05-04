from data.load_dataset import load_dataset
from data.vizualization_dataset import histogram, boxplot, scatterplot, corelation_matrix, intel_vs_amd_performance
from data.data_preprocessing import process_missing_values, clean_data
from models.comparison_table_performance import create_comparison_table

from services.content_based_filtering import content_based_filtering
from services.topsis import topsis_method
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)




user_features = {
    "brand": "Intel",
    "model": "Intel Core i9-12900KS",
    "category": "",
    "budget": 700,
    "performance": 30000,
    "cores": 8
}

print("\nModel Evaluation:\n")

create_comparison_table()

