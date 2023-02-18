conda create --prefix ./venv python
conda activate venv/

create requirements.txt
create README.md

pip install -r requirements.txt

download the dataset from kaggle : winequality

git init
dvC init

dvc add ./data_given/winequaltiy.csv

git add .
git commit -m " fisrt commit"


git rm -r --cached .   # to remove all the cache

git remote add origin https://github.com/PradeepPathikayala/simple_app.git

git branch -M main


dvc mertics show
dvc mertics diff

tox commands:
tox init
tox -r # for rebuilidng

pytest command:
pytest -v

setup command:
pip install `e .

build your own package comman:
python setup.py sdist bdist wheel

