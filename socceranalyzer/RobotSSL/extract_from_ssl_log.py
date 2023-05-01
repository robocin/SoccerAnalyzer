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
                
                game_state_name = data['decision']['game_state_name']

                if game_state_name == 'Halt':
                    continue

                data_line['game_state_name'] = game_state_name

                data_line['timestamp'] = timestamp

                ball_data = process_frame['ball']

                if 'position' in ball_data and 'velocity' in ball_data and 'acceleration' in ball_data:
                    data_line['ball_position_x'] = ball_data['position']['x']
                    data_line['ball_position_y'] = ball_data['position']['y']

                    data_line['ball_velocity_x'] = ball_data['velocity']['x']
                    data_line['ball_velocity_y'] = ball_data['velocity']['y']

                    data_line['ball_acceleration_x'] = ball_data['acceleration']['x']
                    data_line['ball_acceleration_y'] = ball_data['acceleration']['y']
                else:
                    continue
                
                allies = process_frame['allies']
                enemies = process_frame['enemies']

                if (len(allies) == 6 and len(enemies) == 6):
                    for ally in allies:
                        id = str(ally['id'])

                        data_line[f'ally_{id}_position_x'] = ally['position']['x']
                        data_line[f'ally_{id}_position_y'] = ally['position']['y']

                        data_line[f'ally_{id}_velocity_x'] = ally['velocity']['x']
                        data_line[f'ally_{id}_velocity_y'] = ally['velocity']['y']

                    for enemy in enemies:
                        id = str(enemy['id'])

                        data_line[f'enemy_{id}_position_x'] = enemy['position']['x']
                        data_line[f'enemy_{id}_position_y'] = enemy['position']['y']

                        data_line[f'enemy_{id}_velocity_x'] = enemy['velocity']['x']
                        data_line[f'enemy_{id}_velocity_y'] = enemy['velocity']['y']
                else:
                    continue

                frame_data.append(data_line)
        
        data_frame = pd.DataFrame(frame_data)

        return data_frame