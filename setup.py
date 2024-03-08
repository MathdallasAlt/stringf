from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.1'
DESCRIPTION = 'Functions for strings.'
LONG_DESCRIPTION = 'A package that includes various functions for strings.'

# Setting up
setup(
    name="stringf",
    version=VERSION,
    author="Mathdallas_code(Jaiwant morampudi)",
    author_email="<krishnapacs255@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['python','string','functions'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)