from setuptools import setup, find_packages

setup(
    name='socceranalyzer',
    description='2DSIM, VSS and SSL data analysis package',
    url='https://github.com/robocin/socceranalyzer',
    author='Felipe Nunes, Mateus Soares, Bruna Alves',
    version='1.2.0',
    packages=[package for package in find_packages() if package.startswith("socceranalyzer")],
    install_requires=['pandas', 'numpy', 'seaborn']
)
