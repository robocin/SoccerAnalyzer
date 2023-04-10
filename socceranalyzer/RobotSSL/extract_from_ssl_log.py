import pandas as pd
import numpy as np

class ExtractFromLog:
    def __init__(self, log_list):
        self.log_list = log_list
        
    def extract_frame(self):
        frame_data = []

        for data in self.log_list:
            if 'processed_frame' in data and 'decision' in data:
                process_frame = data['processed_frame']
                data_line = {}
                timestamp = np.int64(process_frame['publish_timestamp'])

                if timestamp == 0:
                    continue

                data_line['game_state_name'] = data['decision']['game_state_name']

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

                frame_data.append(data_line)
        
        data_frame = pd.DataFrame(frame_data)

        return data_frame