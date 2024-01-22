import pandas as pd
import argparse

from socceranalyzer import Match, MatchAnalyzer, SIM2D, JsonReader, YamlReader, RunConfiguration, Logger

def setup():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("run", help="run analysis")
    arg_parser.add_argument("-v", "--version", help="show socceranalyzer version")
    arg_parser.add_argument("-f", "--file", help="configuration file, either json or yml")
    args = arg_parser.parse_args()

    info = YamlReader.read(args.file)
    config = RunConfiguration()
    config.parse(info)
    
    return config

if __name__ == "__main__":
    
    config:RunConfiguration = setup()
    
    dataframe = pd.read_csv(config.file_path)
    match = Match(dataframe, config.category)
    match_analyzer = MatchAnalyzer(match,run_config=config)
    
    adapter = JupyterAdapter(match_analyzer)
    adapter.goalkeeper()
