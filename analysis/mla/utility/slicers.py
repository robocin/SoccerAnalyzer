class PlaymodeSlicer:
    """
        Playmode slicer
    """ 
    @staticmethod
    def slice(dataframe, playmode):
        temp_df = dataframe[dataframe["playmode"] == playmode]
        return temp_df


class CustomSlicer:

    """
        A slicer that can be custom parameterized with a entry and end cycle.
        Return:
            A subset of the given dataframe starting at 'entry_cycle' and ending at 'end_cycle'
    """
    def __init__(self, dataframe, entry_cycle, end_cycle, playmode=None):
        self.__dataframe = dataframe
        self.__playmode = playmode
        self.__entry_cycle = entry_cycle
        self.__end_cycle = end_cycle

    def slice(self):
        pass
