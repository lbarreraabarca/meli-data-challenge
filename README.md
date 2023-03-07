# MELI Data Challenge

This application solve some challenges proposed by MELI team. Also, this app read data from csv and json files stored on [src/resources/data](https://github.com/lbarreraabarca/meli-data-challenge/tree/main/src/resources/data). As well, this app was develop in Python using dependencies defined on [src/requirements.txt](https://github.com/lbarreraabarca/meli-data-challenge/blob/main/src/requirements.txt). Regarding the solutions we can find on [output/](https://github.com/lbarreraabarca/meli-data-challenge/tree/main/output) folder. 


## How to use

### GitHub Actions
The pipeline has runned in GitHub Actions workers. If we want execution details we can see [GitHub Actions](https://github.com/lbarreraabarca/meli-data-challenge/actions).
On the other hand, the main solution is [src/App.py](https://github.com/lbarreraabarca/meli-data-challenge/blob/main/src/App.py) if we want to test the solution local way. So, we must execute the following steps:

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