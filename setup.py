#!/usr/bin/env python
from setuptools import setup, find_packages
import importlib.util
from os import path as op
import io

spec = importlib.util.spec_from_file_location("version", "version.py")
version = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version)
__version__ = version.__version__
here = op.abspath(op.dirname(__file__))
with open(op.join(here, "README.md")) as fp:
    long_description = fp.read()
with io.open(op.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")
install_requires = [x.strip() for x in all_reqs if "git+" not in x]
dependency_links = [x.strip().replace("git+", "") for x in all_reqs if "git+" not in x]

setup(
    name="scripts_py_template",
    author="DevSeed",
    author_email="devseed@developmentseed.org",
    version=__version__,
    description="Template for python script",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/developmentseed/scripts_py_template",
    keywords="",
    entry_points={"console_scripts": ["read_file = scripts_py_template.main:main"]},
    packages=find_packages(exclude=["docs", "tests*"]),
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
)
