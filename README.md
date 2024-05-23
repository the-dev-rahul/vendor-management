# VendorManagement

## Python Version 
- 3.9

## Create Virtual Environemnt
'''
python3 -m venv venv
source ./venv/bin/activate
'''


## install requirements
'''
python install -r ./requirements.txt
'''

## Setup Postgres DB

# Create .env 
'''
copy env_sample .env
'''

### Add environment variables in .env files

## Run migrate commmand
''' python manage.py migrate '''

## Run server
''' python manage.py runserver '''

## Check Swagger
''' {hots}/swagger/ '''