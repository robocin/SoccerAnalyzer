from setuptools import setup, find_packages

setup(
    name='socceranalyzer',
    version='2.0.0',
    description='Robocup Soccer data analysis package for SIM2D, SSL and VSS categories',
    url='https://github.com/robocin/SoccerAnalyzer',
    author='RoboCIn',
    author_email="robocin@cin.ufpe.br",
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Jupyter',
        'Framework :: Matplotlib',
        'Framework :: Robot Framework :: Library',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.10',
    ],
    keywords="data science analysis robotics jupyter matplotlib pandas",
    project_urls={
        'Documentation': 'TBA',
        'Source': 'https://github.com/robocin/SoccerAnalyzer',
        'Tracker': 'https://github.com/robocin/SoccerAnalyzer/issues'
    },
    packages=[package for package in find_packages() if package.startswith("socceranalyzer")],
    install_requires=['pandas', 'numpy', 'matplotlib', 'seaborn'],
    python_requires='>3.10.*'
)
