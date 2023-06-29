import pickle

SQL_QUERY = """
    SELECT * from customer
    LEFT JOIN city USING(zip_code)
    LEFT JOIN account USING(customer_id)
    LEFT JOIN account_usage USING (account_id)
    LEFT JOIN churn_status USING (customer_id)
    where churn_label IS NOT NULL
"""
CSV_PATH = 'data/example_csv_path.csv'

TARGET_COL = 'churn_label'


CATBOOST_MODEL_FILEPATH = "model/catboost_model.pkl"

best_params_file_path = "model/catboost_best_params.pkl"
# Load the best params from the pickle file
with open(best_params_file_path, 'rb') as f:
    CATBOOST_BEST_PARAMS = pickle.load(f)

RANDOM_SEED = 42
TEST_SIZE = 0.3
optimal_threshold_path = "model/optimal_threshold.pkl"
# Load the optimal threshold from the pickle file
with open(optimal_threshold_path, 'rb') as f:
    OPTIMAL_THRESHOLD = pickle.load(f)