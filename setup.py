from setuptools import setup, find_packages

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='AnalyzerCommon',
    version='1.0',
    packages=find_packages(),
    install_requires=install_requires
)
