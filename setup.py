from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.7'
DESCRIPTION = 'Functions for strings and lists'
LONG_DESCRIPTION = '''
Current version-0.0.7
String:
    -NEW-
    Added list_to_str(list) function
    Fixed module not importing bug
    A package that has several functions to work with strings and English words.
    Functions-

    plural-Converts any word to plural form.
    e.g. plural("python")-"pythons"

    join: joins two words e.g. 'pyt','hon'-'python'

    add: Like the join() functions but can join word after the letter at the specified position
    e.g. add("bore",1,"ef")-'before'

    reverse: Reverses a string 
    e.g. reverse("python")-"nohtyp"

Lists:
    list_to_str: Convert a list into a string e.g. ['p','y','t','h','o','n']-'python'

More functions coming soon!
'''

# Setting up
setup(
    name="stringf",
    version=VERSION,
    author="Mathdallas_code(Jaiwant Morampudi)",
    author_email="<krishnapacs255@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python','string','English','words','functions'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)