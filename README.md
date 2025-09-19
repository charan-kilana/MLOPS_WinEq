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
