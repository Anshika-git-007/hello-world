# What is this for:

This is a simple Python/Flask application intended to provide a working example of 

# How to use:
Run pip install -r requirements.txt to install dependencies
Run python app.py
Navigate to http://localhost:7000 in your browser

# Testing:

Install the dependencies with make bootstrap
Run the command make test
If you delete the fixtures, or decide to add some of your own, you’ll have to re-generate them, 
and the way this is done is by running the app, getting an auth_token from the main page of the app. Paste that token in place of the test_auth_token at the top of the test_endpoints.py file, then run the tests.
