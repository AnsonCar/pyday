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
pip install flit
pip freeze > requirements.txt

# flit build
# python3 -m twine upload --repository testpypi dist/*

# python3 -m pip install --upgrade build
# python3 -m pip install --upgrade twine

# pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple pyday-AnsonCar==0.0.17

# touch pyproject.toml
# git clone https://github.com/pyecharts/pyecharts-gallery.git