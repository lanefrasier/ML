from pyspark.sql import SparkSession
from itertools import product

spark = SparkSession.builder.appName("JoinLargeDatasets").getOrCreate()

# Load datasets into Spark DataFrames
sap_sdf = spark.read.csv('sap january.csv', header=True, inferSchema=True)
sfmc_sdf = spark.read.csv('sfmc january.csv', header=True, inferSchema=True)

# Perform the join
pairs_sdf = sap_sdf.crossJoin(sfmc_sdf)

# Save the result back to storage
pairs_sdf.write.csv('pairs_data', header=True)

""" 
# Load the saved DataFrames
sap_df = pd.read_pickle('sap_data.pkl')
sfmc_df = pd.read_pickle('sfmc_data.pkl')

# Generate all possible pairs of SAP and SFMC records
sap_df['key'] = 1
sfmc_df['key'] = 1
pairs = pd.merge(sap_df, sfmc_df, on='key').drop('key', axis=1)
print(pairs.columns)
# Rename columns for clarity
pairs = pairs.rename(columns={
    'Mobile_x': 'sap_mobile', 'Mobile_y': 'sfmc_mobile',
    'Send Date_x': 'sap_date', 'Send Time_x': 'sap_time', 'Send Date_y': 'sfmc_date', 'Send Time_y': 'sfmc_time',
    'Brand Name_x': 'sap_brand', 'Brand Name_y': 'sfmc_brand', 'Message Description_x': 'sap_desc', 'Message Description_y': 'sfmc_desc'
})

#Combine date and time columns
pairs['sap_datetime'] = pd.to_datetime(pairs['sap_date'] + ' ' + pairs['sap_time'])
pairs['sfmc_datetime'] = pd.to_datetime(pairs['sfmc_date'] + ' ' + pairs['sfmc_time'])

pairs.to_csv(r'C:/Users/LFrasier/OneDrive - NRG Energy, Inc/Desktop/Code/ML/pairs_data.csv', index=False)"""

print("Generated Pairs:\n", pairs_sdf.head()) 