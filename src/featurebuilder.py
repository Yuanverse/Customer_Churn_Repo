import numpy as np
import pandas as pd
from datapreprocessor import Data_Preprocessor
from config import TARGET_COL

class FeatureBuilder:
    '''
    This class uses DataPreprocessor to clean data during __init__.
    Underscore prefix used for internal-access methods.
    Feature Engineering steps are documented in:
    build_train_set() and build_test_set().
    '''

    def __init__(self, df):
        self.df = Data_Preprocessor(df).get_clean_dataset()
        self._validate_df()
        self._excluded_cols = [TARGET_COL, 'customer_id', 'account_id', 'zip_code', 'area_id', 'latitude', 'longitude']

    def build_train_set(self):
        '''
        Returns model_input (X) and labels (y) for training.
        Requires target column to be present
        '''
        self._add_features()
        X = self.df.drop(columns=self._excluded_cols, errors='ignore')
        y = self.df[TARGET_COL]
        return X, y
    
    def build_test_set(self):
        '''Returns model_input (X) for predictions.'''
        self._add_features()
        X = self.df.drop(columns=self._excluded_cols, errors='ignore')
        return X

    def _validate_df(self):
        df_cols = self.df.columns
        check_columns = ['total_refunds', 'total_charges_quarter', 'num_dependents', 'avg_gb_download_monthly', 'tenure_months']
        for col in check_columns:
            assert col in df_cols, f"Required column {col} not found. " \
                f"List of Dataset Columns: {list(df_cols)}"

    def _add_features(self):
        self.df['total_long_distance_fee'] = self.df['avg_long_distance_fee_monthly'] * self.df['tenure_months']
        
        self.df['refund_ratio_qtr'] = np.log1p(self.df['total_refunds'].astype(float)) - np.log1p(self.df['total_charges_quarter'].astype(float))
        
        self.df['total_long_distance_fee_per_dependant'] = np.log1p(self.df['total_long_distance_fee'].astype(float)) - np.log1p(
            self.df['num_dependents'].astype(float))
        
        self.df['total_gb_downloaded'] = self.df['avg_gb_download_monthly'] * self.df['tenure_months']


