rem Create the Package
python setup.py sdist bdist_wheel

rem Upload it to PyPI
twine upload --config-file .pypirc dist/*

rem Cleanup
rmdir /Q /S CardGameBase.egg-info\
rmdir /Q /S build\
rmdir /Q /S dist\
