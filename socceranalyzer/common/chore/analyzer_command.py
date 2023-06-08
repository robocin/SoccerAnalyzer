from socceranalyzer.common.chore.match_analyzer import MatchAnalyzer
from socceranalyzer.common.io.reader import FolderReader
from socceranalyzer.common.io.tester import Tester
from socceranalyzer.utils.logger import Logger
from socceranalyzer.utils.run_configuration import ExecutionType, RunConfiguration

class AnalyzerCommand:
    @staticmethod
    def execute(config: RunConfiguration, match_analyzer: MatchAnalyzer):
        if config.execution == ExecutionType.RUN:
            Logger.warn("Implement run execution.")
        if config.execution == ExecutionType.TESTER:
            Logger.info(f"Searching for files in {config.logs_dir}")
            rcg_files = FolderReader.read(config.logs_dir)
            Tester.statistics_from_filenames(rcg_files)
            Tester.log(rcg_files)
            Tester.save_to_file()