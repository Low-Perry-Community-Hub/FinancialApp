# Setup Guide for FinancialApp

## Prerequisites
1. **Python 3.8+** installed on your system.
2. A **GitHub account** to clone the repository.
3. **Basic command-line knowledge** to run scripts.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YourOrgName/FinancialApp.git
   cd FinancialApp


## Create and activate a virtual environment:
1. python3 -m venv venv
2. source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows


## Install Dependencies
1. pip install -r requirements.txt


## Initialize the database
1. python database/setup.py

## Run the app:
1. uvicorn api.main:appp --reload

## Access the API:
1. Open your browser and go to: http://127.0.0.1:8000

