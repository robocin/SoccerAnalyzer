## SoccerAnalyzer CLI
This feature provides the user to calculate simple metrics on top of the .rcg files
produced by rcssserver.

### How to use?
By default, an instance of socceranalyzer.CLI will collect all .rcg files in the given directory, process them and calculate the metrics.
```python
from socceranalyzer import CLI

RCG_FILES_PATH = ""

cli = CLI(RCG_FILES_PATH)
cli.log()
```