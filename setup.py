import setuptools

import io
import os
import re

with io.open('lru/version.py', 'rt', encoding='utf-8') as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lruheap",
    version=version,
    author="Ryan Febriansyah",
    author_email="15523163@students.uii.ac.id",
    description="Python decorators for store in-data memory using LRU cache",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sodrooome/lru-cache",
    license='MIT',
    zip_safe=False,
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.5',
)