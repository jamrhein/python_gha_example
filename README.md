# AWESOME CALCULATOR

![Awesome Calculator CI build](https://github.com/dedreira/awesomecalculator/workflows/Awesome%20Calculator%20CI%20build/badge.svg)
## What is this project about?

It's a very basic project that shows how to set up a python package that contain a really basic calculator service.

It uses GitHub actions to fire a CI build that run the tests and generate the package with the calculator

The package has been created following this [tutorial](https://packaging.python.org/tutorials/packaging-projects/)

## Python version:
**3.7**

## Folder structure

1. __/.github/workflows__
    This folder will contain the GitHub workflows template

2. __/src__
    This folder will contain the source code of the awesome calculator package :smile:

## Unit Tests

This project uses [unittest](https://docs.python.org/3/library/unittest.html) as the testing framework, and [coverage.py](https://coverage.readthedocs.io/en/coverage-5.4/) for generating code coverage reports.

### How to run the unit tests

Inside the __/src__ folder, just run this command:

````bash
python -m unittest -v
````
### How to view the coverage report

Inside the __/src__ folder, just run this command:

````bash
coverage run -m unittest
````

and to report on the results:
````bash
coverage report
````


