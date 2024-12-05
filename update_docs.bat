cd docs
sphinx-apidoc -o source/ ../
sphinx-build -b html source/ build/html
