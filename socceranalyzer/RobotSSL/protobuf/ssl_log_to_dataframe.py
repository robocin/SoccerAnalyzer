import protobuf.generated.RCLog as ProtoRCLog
from pyrecordio.compressed_proto_record_reader import CompressedProtoRecordReader as ProtoRecordReader
from betterproto import Casing
import pandas as pd
import numpy as np
import proto_compiler.auto_generate_proto as auto_generate_proto

class LogToDataframe:
    def __init__(self, log_path):
        self.log_path = log_path
        self.log_data = []
        self.modules = ['raw_frame', 'raw_referee', 'processed_frame', 'telemetry', 'decision', 'behavior',
                        'planning', 'navigation']

        auto_generate_proto.generate_proto_classes()
        self.extract_data()

    def extract_data(self):
        with open(self.log_path, "rb") as inp:
            reader = ProtoRecordReader(inp, ProtoRCLog.Log)

            for logMsg in reader:
                all_data = logMsg.to_dict(Casing.SNAKE, True)
                select_data = {'timestamp': str(logMsg.timestamp)}

                for modField in self.modules:
                    #data_key = str(modField).lower().split('.')[-1]
                    if modField in all_data:
                        select_data[modField] = all_data[modField]
                
                if len(select_data.keys()) > 1:
                    self.log_data.append(select_data)

    def extract_ball_data(self)-> pd.DataFrame:
        ball_data_list=[]

        for data in self.log_data:
            if 'processed_frame' in data:
                process_frame = data['processed_frame']
                data_line = {}
                timestamp = np.int64(process_frame['publish_timestamp'])

                if timestamp == 0:
                    continue

                data_line['timestamp'] = timestamp

                ball_data = process_frame['ball']

                if 'position' in ball_data:
                    data_line['position_x'] = ball_data['position']['x']
                    data_line['position_y'] = ball_data['position']['y']

                if 'velocity' in ball_data:
                    data_line['velocity_x'] = ball_data['velocity']['x']
                    data_line['velocity_y'] = ball_data['velocity']['y']
                
                if 'acceleration' in ball_data:
                    data_line['acceleration_x'] = ball_data['acceleration']['x']
                    data_line['acceleration_y'] = ball_data['acceleration']['y']

                ball_data_list.append(data_line)
        
        data_frame = pd.DataFrame(ball_data_list)

        return data_frame
    # def frame_dataframe(self):
    #     log = rc_log_pb2.Log()
    #     log.ParseFromString(self.__data)

    #     filtered_field_names = ["decision", "processed_frame"]

    #     filtered_messages = [(field_name, getattr(log, field_name)) for field_name in filtered_field_names if log.HasField(field_name)]

    #     for message_name, message_object in filtered_messages:
    #         print(f"Message: {message_name}")
    #         print(message_object)