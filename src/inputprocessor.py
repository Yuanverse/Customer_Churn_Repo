import numpy as np
import pandas as pd
from config import TARGET_COL
from featurebuilder import FeatureBuilder


class InputProcessor:
    def __init__(self, dataset):
        self.dataset = dataset
        self._feature_type = {
            'gender': str,
            'age': int,
            'senior_citizen': str,
            'married': str,
            'num_dependents': int,
            'area_id': int,
            'city_name': str,
            'population': int,
            'tenure_months': int,
            'num_referrals': int,
            'has_internet_service': str,
            'internet_type': str,
            'has_unlimited_data': str,
            'has_phone_service': str,
            'has_multiple_lines': str,
            'has_premium_tech_support': str,
            'has_online_security': str,
            'has_online_backup': str,
            'has_device_protection': str,
            'contract_type': str,
            'paperless_billing': str,
            'payment_method': str,
            'avg_long_distance_fee_monthly': float,
            'total_long_distance_fee': float,
            'avg_gb_download_monthly': float,
            'stream_tv': str,
            'stream_movie': str,
            'stream_music': str,
            'total_monthly_fee': float,
            'total_charges_quarter': float,
            'total_refunds': float,
            'refund_ratio_qtr': float,
            'total_long_distance_fee_per_dependant': float,
            'total_gb_downloaded': float
        }
        self._feature_list = [feature for feature in self._feature_type.keys() if feature != 'area_id']


    def preprocess_input(self, input_params):
        input_params = self._transform_type_input_params(input_params)
        input_params = pd.DataFrame(input_params, index=[0])
        
        # Check if age is greater than or equal to 65
        age = input_params['age'].values[0]
        input_params['senior_citizen'] = self._check_senior_citizen(age)

        # Retrieve city name and population based on area_id
        area_id = input_params['area_id'].values[0]
        city_name, population = self._get_city_info(area_id)

        # Append city name and population to input_params
        input_params['city_name'] = city_name
        input_params['population'] = population
        
        # Build the test set using FeatureBuilder
        X_test = FeatureBuilder(input_params).build_test_set()

        X_test = X_test[self._feature_list]

        return X_test

    def _transform_type_input_params(self, input_params):
        transformed_params = {}
        for key, value in input_params.items():
            if key in self._feature_type:
                transformed_params[key] = self._feature_type[key](value)
        return transformed_params

    def _check_senior_citizen(self, age):
        if age >= 65:
            return "Yes"
        else:
            return "No"

    def _get_city_info(self, area_id):
        # Retrieve city name and population from self.dataset based on area_id
        city_name = self.dataset.loc[self.dataset['area_id'] == area_id, 'city_name'].values[0]
        population = self.dataset.loc[self.dataset['area_id'] == area_id, 'population'].values[0]

        return city_name, population


    
    

