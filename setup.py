# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = "0.22"


# with open("README.md", "rb") as f:
long_descr = "Work in progress..." #f.read().decode("utf-8")


setup(
    name = "rosshill-physics",
    packages = ["physics"],
    entry_points = {
        "console_scripts": ['physics = physics.physics:start']
        },
    version = version,
    description = "Python command line rocket simulator.",
    long_description = long_descr,
    author = "Ross Hill",
    author_email = "rosshill@protonmail.com",
    url = "http://www.rosshill.ca",
    install_requires=['termcolor','matplotlib'],
    )
