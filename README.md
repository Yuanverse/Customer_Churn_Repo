# TEAM KYJ (may23-team09)

Team Number: 09

Team Logo: ![Logo](./src/static/assets/favicon-32x32.png)

Names of team members:
- Kai Yuan T.
- Jessica G.


# Churn Prediction

A web application for churn prediction in a subscription-based service.

## Overview

Our team works in the data science department of TrustTelecom, one of the largest Telecommunications companies in the United States. As a highly competitive industry, customers have the freedom to choose from various service providers and frequently switch between them. This poses a significant challenge for our company in retaining customers. Acquiring new customers is not only difficult but also costly compared to maintaining existing customer relationships.

Our team has been given the task by higher management to build a customer churn prediction model. The objective is to identify customers who are likely to switch to another service provider in the next month. This will allow our customer care team to proactively reach out to them, understand any frustrations they may have, and provide suitable discounts, offers, and refunds to retain these customers in the long run.

For this capstone project, our team will collaborate to build a machine learning classifier that can predict the likelihood of a specific customer churning. Once we select a model that optimizes the Area Under Curve (AUC) metric, our next step will be to deploy this model for our company's Customer Care team.

## Installation

1. Clone the repository, then Create a Virtual Environment and Activate it:

    ```bash
    git clone https://github.com/Heicoders-AI300/may23-team09.git
    cd may23-team09
    virtualenv venv
    source venv/Scripts/activate
    ```

2. Navigate to cloned repository's directory & Install Dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create .env file in the src folder, paste the below filled-up config details into the .env file (Ensure .env is included in .gitignore for security reasons.)

    ```
    ENDPOINT = ''
    PORT = 
    USERNAME = ''
    DBNAME = ''
    PASSWORD = ""
    CURSORCLASS = pymysql.cursors.DictCursor
    ```

4. Download the pre-trained churn prediction model (catboost_model.pkl) and place it in the "model" directory.

5. Start the webapp.

    ```bash
    python src/main.py
    ```

6. Access the application at http://localhost:5000 in your web browser.

##  Usage

1. HTML Form

    a. Access the application at http://localhost:5000 in your web browser.

    b. Fill in the input fields with the required information. Click the "Submit" button to get the predicted churn probability. The predicted churn probability will be displayed below the form.

2. API endpoint that supports POST request with JSON input

    a. Run the cell in notebooks/send_payload.ipynb to get predictions.

    b. Modify input parameters in notebooks/payload.json. You may add on more inputs.

##  Contributing
Contributions are welcome from team09! If you have any suggestions, bug reports, or want to contribute to the project, please follow these steps:

1. After Cloning, Create a new branch: 
```
git checkout -b feature/your-feature
```

2. Make the necessary changes to implement your feature. Stage the changes and commit it locally:
```
git add . 
git commit -m 'Add your commit message here'
```

3. Push the branch to the remote repository: 
```
git push origin feature/your-feature
```

4. Go to the repository on GitHub https://github.com/Heicoders-AI300/may23-team09

5. Open a pull request by clicking on the "Compare & pull request" button next to your branch.

6. Provide a clear and descriptive title and description for your pull request, explaining the changes you made.

7. Review the changes in the pull request and address any feedback or comments from reviewers.

8. Once the pull request is approved, merge it into the master branch by clicking on the "Merge pull request" button.

9. Optionally, delete the feature branch after it has been merged.


## Website URL of deployed web app 

    URL: http://3.106.128.235/

    Info on final chosen model and parameters: 
    
    33 model_features used: [
        'gender', 'age', 'senior_citizen', 'married', 'num_dependents',
       'city_name', 'population', 'tenure_months', 'num_referrals',
       'has_internet_service', 'internet_type', 'has_unlimited_data',
       'has_phone_service', 'has_multiple_lines', 'has_premium_tech_support',
       'has_online_security', 'has_online_backup', 'has_device_protection',
       'contract_type', 'paperless_billing', 'payment_method',
       'avg_long_distance_fee_monthly', 'total_long_distance_fee',
       'avg_gb_download_monthly', 'stream_tv', 'stream_movie', 'stream_music',
       'total_monthly_fee', 'total_charges_quarter', 'total_refunds',
       'refund_ratio_qtr', 'total_long_distance_fee_per_dependant',
       'total_gb_downloaded'
       ]

    CatBoost Classifier with Best Parameters: {'depth': 6, 'iterations': 200, 'l2_leaf_reg': 3, 'learning_rate': 0.05}
    Optimal Threshold based on f1 score calculated: 0.3

    Offline AUC metrics of Final chosen model: (CatBoost) Cat AUC: 0.9186 vs (RF) 0.8670

##  Contact
If you have any questions, feedback, or want to collaborate, feel free to reach out:

TEAM KYJ Members
1. GitHub: Yuanverse
2. GitHub: heyjessica42

