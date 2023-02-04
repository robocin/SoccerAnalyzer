class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Logger:
    @staticmethod
    def info(message):
        print("[" + Colors.OKBLUE + "INFO" +  Colors.ENDC + "]: " + message)

    @staticmethod
    def warn(message):
        print("[" + Colors.WARNING + "WARN" +  Colors.ENDC + "]: " + message)

    @staticmethod
    def error(message):
        print("[" + Colors.FAIL + "FAIL" +  Colors.ENDC + "]: " + message)

    @staticmethod
    def success(message):
        print("[" + Colors.OKGREEN + " OK " +  Colors.ENDC + "]: " + message)

    @staticmethod
    def data(message):
        print("[" + Colors.HEADER + "DATA" +  Colors.ENDC + "]: " + message)
        