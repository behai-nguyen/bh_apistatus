"""
Installation script for bh-apistatus project.

* Upgrade:

C:\PF\Python310\python.exe -m pip install --upgrade virtualenv 
C:\PF\Python310\python.exe -m pip install --upgrade pip

* Create virtual environment venv:

C:\PF\Python310\Scripts\virtualenv.exe venv

* Install wheel:

.\venv\Scripts\pip.exe install wheel

* Editable install:

venv\Scripts\pip.exe install -e .

* Package:

venv\Scripts\python.exe setup.py bdist_wheel

==> F:\bh_apistatus\dist\bh_apistatus-1.0.0-py3-none-any.whl

* Install package on a new environment:

venv\Scripts\pip.exe install bh_apistatus-1.0.0-py3-none-any.whl

"""

"""
from pathlib import Path
from setuptools import setup, find_packages

setup(
    name='bh-apistatus',
    description='BeHai API Status',
    version='1.0.0',
    author='Van Be Hai Nguyen',
    author_email='behai_nguyen@hotmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires='>=3.10',
    install_requires=[
        'pytest',
        'coverage',
        'sphinx',
        'myst-parser',
        'sphinx-rtd-theme',
        'm2r',
    ],
)
"""

"""
* Editable install:

    (venv) F:\bh_apistatus>venv\Scripts\python.exe -m pip install -e .
    (venv) F:\bh_apistatus>venv\Scripts\pip.exe install -e .

* Install build tools build and twine

    (venv) F:\bh_apistatus>venv\Scripts\pip.exe install build twine

* Build package:

    (venv) F:\bh_apistatus>venv\Scripts\python.exe -m build
    
    ==>

    F:\bh_apistatus\dist\bh_apistatus-1.0.0-py3-none-any.whl
    F:\bh_apistatus\dist\bh-apistatus-1.0.0.tar.gz

* Confirm package build:

    (venv) F:\bh_apistatus>venv\Scripts\twine.exe check dist/*

* Upload to https://test.pypi.org/project/

    (venv) F:\bh_apistatus>twine upload --verbose -r testpypi dist/*

"""
from setuptools import setup

setup()
