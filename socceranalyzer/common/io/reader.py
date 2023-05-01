import json
from socceranalyzer.utils.logger import Logger
from socceranalyzer.utils.run_configuration import RunConfiguration

import sys
sys.path.append('socceranalyzer/RobotSSL/')

from socceranalyzer.RobotSSL.pyrecordio.compressed_proto_record_reader import CompressedProtoRecordReader as ProtoRecordReader
from betterproto import Casing
from socceranalyzer.RobotSSL.proto_compiler import auto_generate_proto
from socceranalyzer.RobotSSL.protobuf.generated import RCLog as ProtoRCLog

class Reader:
    def __init__(self, games=None, games_count=0):
        self._games = games
        self._games_count = games_count

    @staticmethod
    def read(self, path):
        raise NotImplementedError
    
    @staticmethod
    def how_many(self):
        return self._games_count
        
class JsonReader:
    @staticmethod
    def read(path:str):
        try:
            file = open(path)
        except Exception as err:
            Logger.error(f"Could not open {path}: {err}")
            return
        else:
            information_dict = {}
            file_data = json.load(file)
            if JsonReader.isValid(file_data):
                for key, values in file_data.items():
                    information_dict[key] = values
                    
            file.close()
            Logger.info(f"{path} parsed")
            return information_dict

    @staticmethod
    def isValid(file_data):
        for key, value in file_data.items():
            if key == "":
                Logger.error(f"Json invalid argument: {key}")
                return False
            if key == "analysis":
                for analysis_key, analysis_value in value.items():
                    if analysis_key == "" or analysis_value not in [True, False]:
                        Logger.error(f"Json invalid argument: {key}")
                        return False
            
        return True
    
class GzReader:
    @staticmethod
    def read(path:str):
        ssl_modules = ['raw_frame', 'raw_referee', 'processed_frame', 'telemetry', 'decision', 'behavior',
                        'planning', 'navigation']

        try:
            auto_generate_proto.generate_proto_classes()
            
            log_data = []

            with open(path, "rb") as inp:
                reader = ProtoRecordReader(inp, ProtoRCLog.Log)

                for logMsg in reader:
                    all_data = logMsg.to_dict(Casing.SNAKE, True)
                    select_data = {'timestamp': str(logMsg.timestamp)}

                    for modField in ssl_modules:
                        if modField in all_data:
                            select_data[modField] = all_data[modField]
                    
                    if len(select_data.keys()) > 1:
                        log_data.append(select_data)

            return log_data

        except Exception as err:
            Logger.error(f"Could not open {path}: {err}")
            return