rm -r -f ./dist 
flit build
python3 -m twine upload --repository testpypi dist/*