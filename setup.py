from setuptools import setup, find_packages

setup(
    name='socceranalyzer',
    version='2.0.1',
    description='Robocup Soccer data analysis package for SIM2D, SSL and VSS categories',
    long_description= open('README.md').read(),
    long_description_content_type='text/markdown',
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
    include_package_data=True,
    packages=[package for package in find_packages() if package.startswith("socceranalyzer")],
    install_requires=['pandas', 'numpy', 'seaborn', 'matplotlib', 'protobuf', 'betterproto','mdutils']
)
