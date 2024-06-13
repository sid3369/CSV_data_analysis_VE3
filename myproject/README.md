# CSV_data_analysis_VE3
This Django web application allows users to upload CSV files, performs basic data analysis using pandas and numpy, and displays the results and visualizations on the web interface.

STEP 1 : CLONE THE REPOSITORY 
    git clone https://github.com/sid3369/CSV_data_analysis_VE3.git
    
STEP 2 : ACTIVATE THE VIRTUAL ENVIORNMENT
    python -m venv venv
    source venv/bin/activate

STEP 3 : INSTALL ALL THE DEPENDANCIES
    pip install -r requirements.txt

STEP 4 : START THE DEVELOPMMENT SERVER
    python manage.py makemigrations
    python manage.py migrate      
    python manage.py runserver

Open your web browser and navigate to the link generated after running the commands.

NOTE : The visualizations results displayed in this application are specifically based on the dataset provided: india_population_new.csv
