python3 -m venv .venv
source $(pwd)/.venv/bin/activate
pip install --upgrade pip
pip install autopep8
pip install pandas
pip install numpy
pip install matplotlib
pip install pyecharts
pip install notebook
pip install jupyterlab
pip freeze > requirements.txt