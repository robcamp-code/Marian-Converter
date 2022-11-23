import os

import pkg_resources
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Marian-Converter',
    version='0.0.1',
    author='Robert Campbell',
    author_email='',
    description='Onnx-Converter for MarianMT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/robcamp-code/Marian-Converter',
    project_urls = {
        "Bug Tracker": "https://github.com/robcamp-code/Marian-Converter/issues"
    },
    license='MIT',
    packages=['Marian-Converter'],
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
)