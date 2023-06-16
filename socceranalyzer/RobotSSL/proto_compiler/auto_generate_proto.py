import pathlib
import subprocess
import os

def generate_proto_classes():
    proto_description_dir = os.path.join(os.path.dirname(__file__), "../protobuf/pb")
    generated_out_dir = os.path.join(os.path.dirname(__file__), "../protobuf/generated")

    if not os.path.exists(generated_out_dir):
        os.mkdir(generated_out_dir)
        
    proto_src_path = pathlib.Path(proto_description_dir)
    proto_out_path = pathlib.Path(generated_out_dir)

    command = "protoc -I . --python_betterproto_out="+ str(proto_out_path.resolve()) +" rc_log.proto" 

    ret = subprocess.call(command, cwd=str(proto_src_path.resolve()) , shell=True, timeout=10.0)

    if ret != 0:
        print("Error at generating proto classes!")
        raise subprocess.CalledProcessError(ret, command)
