import pandas as pd

# Load SAP dataset
sap_df = pd.read_csv('SAP january.csv')  
# Load SFMC dataset
sfmc_df = pd.read_csv('sfmc january.csv')  

# Save the DataFrames to pickle files
sap_df.to_pickle('sap_data.pkl')
sfmc_df.to_pickle('sfmc_data.pkl')

# Display basic info
print("SAP Dataset:\n", sap_df.head())
print("\nSalesforce Dataset:\n", sfmc_df.head())

