
cd src
python -m coverage run -m unittest
python -m coverage report --omit="*__init__.py,*test*.py"
python -m coverage html --omit="*__init__.py,*test*.py"