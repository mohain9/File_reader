from setuptools import setup, find_packages

setup(
    name='File_reader',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "pandas","datetime","pathlib","streamlit","pandasai","os"    ],)
