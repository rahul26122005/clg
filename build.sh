#!/bin/bash

# Check if virtual environment exists
if [ ! -d "venv" ]; then
  # Create virtual environment
  python3.8 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Verify Python version
python --version

# Install dependencies
pip install -r requirements.txt

# Collect static files
echo "Collect Static..."
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate
