import pandas as pd
import numpy as np
import os
from dataloader import CSV_Loader, SQL_Loader
from featurebuilder import FeatureBuilder
from model.models import CatBoostModel
from model.evaluator import ModelEvaluator
from inputprocessor import InputProcessor
from flask import Flask, request, render_template
from config import TEST_SIZE, RANDOM_SEED, OPTIMAL_THRESHOLD

def load_data():
    return SQL_Loader().load_data()

def evaluate(model, dataset):
    X, y = FeatureBuilder(dataset).build_train_set()
    metrics_dict = ModelEvaluator(model, X, y)\
        .evaluate(ModelEvaluator.supported_metrics)
    for metric, value in metrics_dict.items():
        print(f"{metric} = {round(value, 4)}")
        
def retrain(new_model, new_dataset):
    # Load the new dataset and build the train set
    X_train_new, y_train_new = FeatureBuilder(new_dataset).build_train_set()

    # Train the new model on the new dataset
    new_model = new_model.train(X_train_new, y_train_new)

    # Save the trained model
    new_model.save()

def print_churn_probabilities(model, dataset, input_params):
    input_processor = InputProcessor(dataset)
    df = input_processor.preprocess_input(input_params)

    probabilities = model.predict_proba(df)
    churn_probability = probabilities[0]  # Churn probability
    non_churn_probability = 1 - churn_probability  # Non-churn probability

    # Convert probabilities to percentages
    churn_percentage = np.round(churn_probability * 100, 2)
    non_churn_percentage = np.round(non_churn_probability * 100, 2)

    # Define labels for the classes
    class_labels = ['Not Churned', 'Churned']

    # Create a dictionary with class labels and corresponding percentages
    output = {
        class_labels[0]: non_churn_percentage,
        class_labels[1]: churn_percentage
    }

    # Print the output
    print("\n::: Retrieving Churn Probability Predictions :::")
    for label, percentage in output.items():
        print(f'{label}: {percentage:.2f}%')
    return churn_percentage, non_churn_percentage

app = Flask(__name__, static_folder='static', template_folder='templates')


# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        model = CatBoostModel().load()
        dataset = load_data()
        input_params = request.form.to_dict()

        churn_percentage, non_churn_percentage = print_churn_probabilities(model, dataset, input_params)
        
        # Classify based on the optimal threshold
        if churn_percentage >= OPTIMAL_THRESHOLD * 100:
            churn_label = 'Churned'
        else:
            churn_label = 'Not Churned'

        return render_template('home.html', churn_label=churn_label, prediction=churn_percentage, non_prediction=non_churn_percentage)
    
    return render_template('home.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()

    # Load the model and dataset
    model = CatBoostModel().load()
    dataset = load_data()

    # Get the payloads from the request data
    payloads = request_data['data']
    
    # Generate predictions for all payloads using a list comprehension
    predictions = [print_churn_probabilities(model, dataset, payload) for payload in payloads]
    
    # Format the predictions as a list of dictionaries
    response_data = {
        'predictions': [
            {
                'churn_label': 'Churned' if churn_percentage >= OPTIMAL_THRESHOLD * 100 else 'Not Churned',
                'churn_percentage': churn_percentage,
                'non_churn_percentage': non_churn_percentage
            }
            for churn_percentage, non_churn_percentage in predictions
        ]
    }

    return response_data, 200

app.config["DEBUG"] = True

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")  # default





    
    
    
    

 