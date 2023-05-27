touch pyproject.toml
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

# git clone https://github.com/pyecharts/pyecharts-gallery.git
# python3 -m pip install --user --upgrade setuptools wheel twine
# python3 -m pip install setuptools wheel twine
# python3 setup.py sdist bdist_wheel

# python3 -m pip install --upgrade build
# python3 -m pip install --upgrade twine
# python3 -m build
# python3 -m twine upload --repository https://pypi.org/pyday/ dist/*
# python3 -m twine upload dist/*--repository


# open ~/.pypirc

# python3 -m pip install --index-url https://pypi.org/pyday/ --no-deps pyday_AnsonCar