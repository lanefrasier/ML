from itertools import product

# Generate all possible pairs of SAP and SF records
sap_df['key'] = 1  # Temporary column for cartesian join
sf_df['key'] = 1
pairs = pd.merge(sap_df, sf_df, on='key').drop('key', axis=1)

# Rename columns for clarity
pairs = pairs.rename(columns={
    'name_x': 'sap_name', 'name_y': 'sf_name',
    'timestamp_x': 'sap_timestamp', 'timestamp_y': 'sf_timestamp'
})

print("Generated Pairs:\n", pairs.head())
