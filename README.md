## 1. Create a seperate environment with python environment 3.10:

```bash
conda create -n wineq python=3.10 -y
```

## 2. Activate the enivronment
```bash
conda activate wineq
```

## 3. Create a requirements.txt file
```bash
touch requirements.txt
```

## 4. Install the requirements.txt 
```bash
pip install -r requirements.txt
```

## 5. Create template.py to create all files required for project with running the python file.
```bash
touch template.py
```

## 6. Run the template.py file so that all required files and folders will be created.
 ```bash
python template.py
```

## 7. Create a folder to keep the data.
```bash
mkdir data_given
```

## 8. Download the data from the drive link below.
```bash
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing
```

## 9. Upload the CSV file in data_given folder which is created just now.


## 10. Now Initialize git & dvc and also add dvc
```bash
git init
dvc init
dvc add data_given/winequality.csv 
git add 'data_given\.gitignore' 'data_given\winequality.csv.dvc'
```
## 11. Now add git for tracking the files.
```bash
# Option 1: Add specific files
git add data_given/.gitignore data_given/winequality.csv.dvc

# Option 2 (Recommended): Add everything
git add .
```

## 12. Commit the message
```bash
git commit -m "committing files of dvc"
```


## 13. In params.yaml file add the project details.

## 14. Push the file into git
```bash
git add .
git commit -m "Adding the parameters in params.yaml"
```

## 15. Add a new file in src
```bash
touch src/get_data.py
```

## 16. Add the get_data.py from GitHub and push it.
```bash
git add .
git commit -m "adding data in get_data.py"
```

## 17. Loading of Data. Create a file load_data.py
```bash
touch src/load_data.py
```

## 18. Add the load stage in the dvc.yaml

Here we're adding only one stage i.e. **Load stage**.  
If we run **`dvc repro`**, it will execute the pipeline starting from this stage. THen a lock will be created and that'll track the file.


```bash
stages:
  load_data:
    cmd: python src/load_data.py --config=params.yaml
    deps:   # Dependencies for this load stage to run.
    - src/get_data.py
    - src/load_data.py
    - data_given/winequality.csv
    outs:   # output of the load stage is csv file without spaces in fields.
    - data/raw/winequality.csv
```

## 19. Splitting of Data. Create a file split_data.py
```bash
touch src/split_data.py
```

## 20. Add the split stage in the dvc.yaml
Here we're adding only one stage i.e. **Split stage**.  
If we run **`dvc repro`**, it will execute the pipeline starting from this stage. THen a lock will be created and that'll track the file.
```bash
split_data:
    cmd: python src/split_data.py --config=params.yaml
    deps:
    - src/split_data.py
    - data/raw/winequality.csv
    outs:
    - data/processed/train_winequality.csv
    - data/processed/test_winequality.csv 
```
touch src/train_and_evaluate.py

## 21. Training the Data. Create a file train_and_evaluate.py
```bash
touch src/train_and_evaluate.py
```

## 20. Add the split stage in the dvc.yaml
Here we're adding only one stage i.e. **Train stage**.  
If we run **`dvc repro`**, it will execute the pipeline starting from this stage. THen a lock will be created and that'll track the file.

```bash
train_and_evaluate:
    cmd: python src/train_and_evaluate.py --config=params.yaml
    deps:
    - data/processed/train_winequality.csv
    - data/processed/test_winequality.csv 
    - src/train_and_evaluate.py
    params:
    - estimators.ElasticNet.params.alpha
    - estimators.ElasticNet.params.l1_ratio
    metrics:
    - report/scores.json:
        cache: false
    - report/params.json:
        cache: false
    outs:
    - saved_models/model.joblib
```

## 21. Create a folder for reports.
```bash
mkdir -p report
```

## 22. Run the dvc repro so that params.json and scores.json are filled.
```bash
touch params.json
touch scores.json
```

## 23. Now we need to track the params.json and scores.json.
```bash
# Displays the metrics i.e scores and params.
dvc metrics show

# Displays the scores diff with previous trained.
dvc metrics diff
```

### TILL HERE YOU CAN EXPERIMENT AND TRAIN THE CODE.

## Note: Generally in real time before they'll test with multiple algorithms in jupyter notebook, once they feel they had better results then they'll start testing in this format like automating.

### 1. From Here in let's do **TESTING**.

## Run tox.ini
```bash
touch tox.ini
```

## 2. Create a folder tests and inside it create conftest.py, test_config.py and __init__.py
```bash
mkdir tests
touch tests/conftest.py        
touch tests/test_config.py         # This is where we define all actuall tests.
touch tests/__init__.py
```

## 3. Any test in test_config.py always run stating with test_name(), example: test_generic()

-- when you run tox then you'll see a seperate file .tox where you'll have multiple env with lib, logs, scripts. It will create all required files in .tox, but next time i.e rebuilding if you update requirements.txt then you should **tox -r**

## 4. Create a setup.py file
``` bash
touch setup.py

# Keep the data in setup.py
pip install -e .
```

<!-- It specifies metadata like the project’s name, version, dependencies, and entry points. You use setup.py when you want to make your project installable via pip, share it on PyPI, or manage dependencies formally for deployment. -->


## 5. Open jupyter-lab notebooks in the cmd
```bash
pip install jupyterlab
jupyter-lab notebooks
```
## 6. flake8, we use for linting  to check the code quality acc to STD.
```bash
pip install flake8

# Also insert the commands to check few syntax in the code in the tox as my file.
# stop the build if there are Python syntax errors or undefined names
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```


## 7. Create a folder for prediction where you need to integrate all prediction related files in that folder so you can call in the application at prediction.
```bash
mkdir -p prediction_service/model
```

## 8. Create a folder for Webapp for the application at prediction.
-- Insert all respective static data onto the webapps.

```bash
mkdir webapp        # Static folder for HTML, CSS, JavaScript files.
mkdir -p webapp/templates
touch webapp/templates/index.html
touch webapp/templates/404.html
touch webapp/templates/base.html
mkdir -p webapp/static/css
mkdir -p webapp/static/script
touch webapp/static/css/main.css
touch webapp/static/script/index.js
touch app.py
touch prediction_service/__init__.py
touch prediction_service/prediction.py
```
## 9. Insert the flask app.
```bash

```








