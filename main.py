import pandas as pd
import argparse
from socceranalyzer import Match, MatchAnalyzer, YamlReader, RunConfiguration, AnalyzerCommand
from socceranalyzer.utils.logger import Logger

def setup():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("run", nargs='?', default=False)
    arg_parser.add_argument("tester", nargs='?', default=False)
    arg_parser.add_argument("-f", "--file", help="configuration file, either json or yml")
    args = arg_parser.parse_args()

    info = YamlReader.read(args.file)
    config = RunConfiguration()
    config.parse(info)
    
    return config

if __name__ == "__main__":
    config:RunConfiguration = setup()
    Logger.enable = True
    
    dataframe = pd.read_csv(config.file_path)
    match = Match(dataframe, config.category)
    match_analyzer = MatchAnalyzer(match,run_config=config)

    AnalyzerCommand.execute(config, match_analyzer)
