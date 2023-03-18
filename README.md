# FirstAPI-MongoDB
# Some GIT commands
set GIT_SSL_NO_VERIFY=true  or git config --global http.sslverify "false" 
update: git config http.sslCAinfo "/path/to/ca-bundle.crt"

git config --global user.name ""
git config --global user.email ""

git pull origin main

new branch
git checkout xxx   switches to new branch xxx
git push origin xxx


git remote add origin https://github.com/drotsen/MongoDB-REST_Api.git
git push -u origin main
# Setting virtual envoirment
python -m venv venv
venv\Scripts\activate.bat

# Alternative 2:
pip install virtualenv
virtualenv [directory]

# Deactivate virtual envoirment
deactivate
# Remove if your virtual environment is in a directory called 'venv':
rm -r venv

# Start uvicorn
uvicorn index:app --reload
http://127.0.0.1:8000/docs   :shows swagger page


# Mongo engine
pip install mongoengine

# Passwrd
pip install passlib[bcrypt] 
pip install python-jose[cryptographic]

# Key secret
openssl rand -hex 32