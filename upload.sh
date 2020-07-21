python setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*
rm -rf dist
rm -rf build
rm -rf alcom.egg-info