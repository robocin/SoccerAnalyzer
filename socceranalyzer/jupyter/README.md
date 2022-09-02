# What is the SoccerAnalyzer Jupyter Adapter?

It enscapsulates matplotlib plottings implementations with the data collected and processed through the MatchAnalyzer. It plots the data from the calculated analysis into matplotlib and display it in the most appropriate way. 

## How to use it?
To understand to use lets quickly recap how does the SoccerAnalyzer works.

### How does the SoccerAnalyzer works?
SoccerAnalyzer orbits around four main structures.
- Dataframe: a pandas object from the game log.
- Match: A representation of an match, defined by the dataframe.
- Category: leagus attribute mappings, which can be from SSL, SIM2D, VSS or any other, that also specifies from which league the current Match is.
- MatchAnalyzer: a class that represents a faccade of available analysis. 
**Match analyzer** is the most important of those, because it is responsible for calculating and interfacing with the available analysis.

## Step by step
### Step 1: Import used structures
```Python
import pandas as pd
from socceranalyzer import Match, MatchAnalyzer, SIM2D, JupyterAdapter
```

### Step 2: Build a dataframe from a .csv
```Python
dataframe = pd.read_csv(PATH_TO_CSV)
```

### Step 3: Instantiace a match and analyze it
```Python
match_object = Match(dataframe, SIM2D)
analyzer = MatchAnalyzer(match_object)
```

### Step 4: Use the JupyterAdapter with MatchAnalyzer
```Python
adapter = JupyterAdapter(analyzer)
```
All plottings can be called using JupyterAdapter instance. To know which analysis are available from the Adapter, use:
```Python
help(adapter)
```

## Quick usage
```Python
import pandas as pd
from socceranalyzer import Match, MatchAnalyzer, SIM2D, JupyterAdapter

PATH_TO_CSV = ""
dataframe = pd.read_csv(PATH_TO_CSV)

match_object = Match(dataframe, SIM2D)
analyzer = MatchAnalyzer(match)

adapter = JupyterAdapter(analyzer)

adapter.ball_possession()
adapter.playmodes()
adapter.fault_position()
adapter.heatmap(ball=True)
adapter.stamina(left_players_unum=[8,9,10])
adapter.plot_shot_log()
adapter.plot_shot_frequency()
adapter.plot_shot_quality()
```