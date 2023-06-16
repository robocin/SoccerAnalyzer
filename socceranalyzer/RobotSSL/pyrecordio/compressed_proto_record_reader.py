import zlib
import sys

sys.path.append('socceranalyzer/RobotSSL/')
from proto_compiler import auto_generate_proto
auto_generate_proto.generate_proto_classes()
import protobuf.generated.RCLog as ProtoRCLog

class CompressedProtoRecordReader:
    __MAGIC_NUMBER = 0x3ed7230a

    def __init__(self, file, proto_class):
        self.file = file
        self.proto_class = proto_class

    def __iter__(self):
        return self

    def __next__(self) -> ProtoRCLog.Log:
        while True:
            header = self.file.read(20)
            if not header:
                break

            magic_number = int.from_bytes(header[:4], "little")
            if magic_number != CompressedProtoRecordReader.__MAGIC_NUMBER:
                continue
            uncompressed_size = int.from_bytes(header[4:12], "little")
            compressed_size = int.from_bytes(header[12:], "little")
            compressed_data = self.file.read(compressed_size)
            try:
                data = zlib.decompress(compressed_data)
                if len(data) != uncompressed_size:
                    raise ValueError("Decompressed data size mismatch")
            except:
                continue

            return self.proto_class.FromString(data)
        
        raise StopIteration