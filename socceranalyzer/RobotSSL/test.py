from protobuf.ssl_log_to_dataframe import LogToDataframe

#place log path below
log_path = ''

log_to_dataframe = LogToDataframe(log_path)

frame = log_to_dataframe.extract_ball_data()

print(frame)