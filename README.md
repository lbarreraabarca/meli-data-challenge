# MELI Data Challenge

This application solve some challenges proposed by MELI team. Also, this app read data from csv and json files stored on `src/resources/data`. As well, this app was develop in Python using dependencies defined on `src/requirements.txt`. Regarding the solutions we can find on `output/` folder. 


## How to use
If we want to test the solution local way. So, we must execute the following steps:

### App

```bash
python3 -m venv venv                # Create a virtualenv
source venv/bin/activate            # Activate virtualenv
pip install -r src/requirements.txt # Install python dependencies
cd src
python App.py                       # Run solution
```

### Unit test 
If we want to run unit test, we could run the following steps:

```bash
bash scripts/check-code.sh      # If you want to validate syntax code.
bash scripts/check-coverage.sh  # If you want to run unit test.
```