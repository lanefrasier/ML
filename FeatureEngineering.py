from sklearn.metrics import pairwise_distances
from datetime import datetime
import numpy as np
import pandas as pd

features_df = pd.read_csv('pairs_data.csv')

# Ensure the columns have string values and handle missing values
features_df['SAP Alert ID'] = features_df['SAP Alert ID'].fillna('').astype(str)
features_df['SFMC Alert ID'] = features_df['SFMC Alert ID'].fillna('').astype(str)

# Calculate the name similarity using set-based Jaccard similarity
features_df['name_similarity'] = features_df.apply(
    lambda row: 1 - (
        len(set(row['SAP Alert ID']) ^ set(row['SFMC Alert ID'])) / 
        max(len(row['SAP Alert ID']), len(row['SFMC Alert ID'])) if max(len(row['SAP Alert ID']), len(row['SFMC Alert ID'])) > 0 else 1
    ), 
    axis=1
)

# Time difference (in seconds)
features_df['time_diff'] = features_df.apply(
    lambda row: abs((pd.to_datetime(row['sap_datetime']) - pd.to_datetime(row['sfmc_datetime'])).total_seconds()), axis=1)

# Metadata Matching: Mobile 
features_df['mobile_match'] = features_df.apply(
    lambda row: 1 if row['sap_mobile'] == row['sfmc_mobile'] else 0, axis=1
)

# Metadata Matching: Brand Name
features_df['brand_match'] = features_df.apply(
    lambda row: 1 if row['sap_brand'] == row['sfmc_brand'] else 0, axis=1
)
print("Pairs with Features:\n", features_df[['SAP Alert ID', 'SFMC Alert ID', 'name_similarity', 'time_diff', 'mobile_match', 'brand_match']].head())

features_df.to_pickle('features_data.pkl')
