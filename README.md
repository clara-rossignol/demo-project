[![Generic badge](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](README.md)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

# GitHub BIO-210 demo project 

This project's goal is to illustrate how GitHub can be used to develop a software project (roughly) following the evolution in BIO-210, but with less code.  

# Contributions Welcome! 

This is an openly developed project and we welcome community contributions, especially from BIO-210 students!
We are happy to receive code extensions, bug fixes, documentation updates, etc.
If you are a new user, we recommend checking out the detailed Github Guides.

# Requirements

- Python >= 3.5
- numpy
- scipy 
- matplotlib

Specifially, I'm sharing a requirements file (req.txt)

`conda create -n <environment-name> --file req.txt`


# Testing

We use [doctests](https://docs.python.org/3/library/doctest.html) and [pytest](https://docs.pytest.org/en/6.2.x/contents.html). 

## Doctests

You can (doc)test the LotkaVolterraModel by:

```python3 LotkaVolterraModel.py ```

It should have no output (if all tests pass). 

You can also get a detailed output pass verbose flag:

```python3 LotkaVolterraModel.py -v```

## Pytests 

We also created unit-tests for the `LotkaVolterraModel.py` in `test_LVM.py`. You can also run the whole test-suite with 

```pytest```

## Coverage 

You can assess the coverage by running:

```
coverage run -m pytest
coverage report
```

This is also available via a bash script `./tests.sh`.