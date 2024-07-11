

#!/bin/bash

# Create a virtual environment
python3.9 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
# pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Deactivate the virtual environment
deactivate







# pip install -r requirements.txt
# python3.9 manage.py collectstatic
