# Start with a python base image
# Take your pick from https://hub.docker.com/_/python
FROM python:3.11-slim

# Set /flask-app as the main application directory
WORKDIR /customer_churn_repo

# Copy the requirements.txt file and required directories into docker image
COPY ./requirements.txt /customer_churn_repo/requirements.txt
COPY ./src /customer_churn_repo/src
COPY ./model /customer_churn_repo/model

# Add /src directory to PYTHONPATH, so that model.py Python module can be found
# To add multiple directories, delimit with colon e.g. /flask-app/src:/flask-app
ENV PYTHONPATH /customer_churn_repo/src

# Install python package dependancies, without saving downloaded packages locally
RUN pip install -r /customer_churn_repo/requirements.txt --no-cache-dir

# Allow port 80 to be accessed (Flask app)
EXPOSE 80

# Start the Flask app using gunicorn
CMD ["gunicorn", "--bind=0.0.0.0:80", "src.app:app"]