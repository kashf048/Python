# https://pypi.org

# pip install requests
# pip install --upgrade pip
# pip install request==2.32.3
# pip install request==2.32.*
# pip uninstall request
# pip install request~=2.*

import requests

response =  requests.get("http://google.com")
print(response)



# VIRTUAL ENVIRONMENT
# python -m venv env
# env\Scripts\activate.bat  
# python install requests==2.32.*
# deactivate

# PIPENV
# pip install pipenv
# pipenv install requests
# pipenv --venv      this is the path of virtual env   C:\Users\kashf\.virtualenvs\Python_Package_Index-wleuy8nz
# pip uninstall requests
# python pip.py
# pipenv shell
# python pip.py
# exit          deactivated



# VIRTUAL ENVIRONMENT IN VS CODE
# pipenv --venv




# PIPFILE
# pipenv install --ignore-pipfile



# MANAGING DEPENDENCIES
# pipenv graph
# pipenv update --outdated




# PUBLISHING PACKAGES
# pypi.org              create account or register
# 