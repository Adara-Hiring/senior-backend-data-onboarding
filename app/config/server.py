import connexion
import unittest
import argparse
import os

swagger_path = './swagger/'
# Create the application instance
app = connexion.FlaskApp("tech_test", specification_dir=swagger_path)

# Read the config files to configure the endpoints
for yml_file in [i for i in os.listdir(swagger_path) if '.yml' in i]:
    app.add_api(yml_file)