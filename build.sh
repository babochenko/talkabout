rm -rf dist/
python -m build

yes | pip uninstall talkabout
pip install dist/*.whl

