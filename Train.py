import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Load your features data
df = pd.read_pickle('features_data.pkl')

# Define features and target
X = df[['time_diff', 'name_similarity', 'mobile_match', 'brand_match']]  # Replace with your feature columns
y = df['is_match']  # Binary target column

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train LightGBM
lgb_train = lgb.Dataset(X_train, y_train)
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

params = {
    'objective': 'binary',
    'metric': 'binary_error',
    'boosting_type': 'gbdt',
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9
}

# Train the model with early stopping
model = lgb.train(
    params,
    lgb_train,
    valid_sets=[lgb_train, lgb_eval],  # Pass training and validation datasets
    valid_names=['train', 'valid'],   # Name the datasets for better logging
    num_boost_round=100,
    callbacks=[
        lgb.early_stopping(stopping_rounds=10),
        lgb.log_evaluation(period=1)]
)

# Predict and evaluate
y_pred = (model.predict(X_test) > 0.5).astype(int)
print("Accuracy:", accuracy_score(y_test, y_pred))
