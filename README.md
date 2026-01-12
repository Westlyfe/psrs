## Project Setup Instructions

Create a virtual environment by running:

python -m venv test

Navigate to the virtual environment directory:

cd test

Activate the virtual environment:

For Linux / macOS:
source bin/activate

For Windows:
test\Scripts\activate

After activating the environment, install the required dependencies:

pip install -r requirements.txt

Once the installation is complete, run the following commands to set up and start the project:

python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver  

Hint:  
Make sure you have already created a database with the name **hospital** before running the migrations.
