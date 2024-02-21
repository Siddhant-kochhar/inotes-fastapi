#to create a virtual environment
python3 -m venv env

# to activate env
source ./env/bin/activate

# to deactivate env
deactivate

## to start server
uvicorn main:app --reload 
