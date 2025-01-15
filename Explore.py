import pandas as pd

# Load the SAP dataset
sap_df = pd.read_csv('SAP january.csv')  # Replace with your file path
# Load the Salesforce dataset
sf_df = pd.read_csv('sfmc january.csv')  # Replace with your file path

# Display basic info
print("SAP Dataset:\n", sap_df.head())
print("\nSalesforce Dataset:\n", sf_df.head())
