from json import dumps

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

class Utility:
    """
    Utiliy class with static methods.
    """    
    @staticmethod
    def slice(dataframe, playmode):
        """
            Slices the dataframe with given playmode.

                Parameters:
                        dataframe (pandas.DataFrame): dataframe to slice
                        playmode (str): string indicating the playmode

                Returns:
                        dataframe (pandas.DataFrame): New sliced dataframe
        """ 
        temp_df = dataframe[dataframe["playmode"] == playmode]
        return temp_df

    @staticmethod
    def find_first_unique_event_ocurrences(dataframe, event): # probably inefficient ? O(n)
        event_ocurrences_index = []
        for i in range(len(dataframe)):
            if(event in dataframe.iloc[i, 1] and event not in dataframe.iloc[i - 1, 1]):
                event_ocurrences_index.append(i)

        return event_ocurrences_index

    @staticmethod
    def find_last_unique_event_ocurrences(dataframe, event): # probably inefficient ? O(n)
        event_ocurrences_index = []
        for i in range(len(dataframe)):
            if(event in dataframe.iloc[i, 1] and event not in dataframe.iloc[i - 1, 1]):
                while dataframe.iloc[i, 1] == event:
                    i += 1
                    if dataframe.iloc[i, 1] != event:
                        event_ocurrences_index.append(i)

        return event_ocurrences_index

    @staticmethod
    def find_unique_event_count(dataframe, event): # not working
        event_ocurrences_index = []
        serie = dataframe[dataframe['playmode'] == event]
        
        for i in range(len(serie)):
            if(serie.iloc[i] != serie.iloc[i-1]):
                event_ocurrences_index.append(i)

        return event_ocurrences_index

    @staticmethod
    def df_count_duplicates(df, column_label):
        """
        Counts the duplicate rows by an specified column and what was the quantity
        :param df: dataframe
        :param column_label: column label you want to look for duplicates
        :return: json string with the duplicates and its quantities

        ex: lets say you have the following df:
        >> df
        show_time   value
        1             A
        2             B
        2             C
        3             D
        4             E
        4             F
        4             G
        5             G
        6             I
        >> json_string = df_count_duplicates(df, 'value')
        >> json_string
        {
            2: 2,
            4: 3
        }

        # ou seja, a linha cuja show_time era 2 apareceu duas vezes e a linha cuja sowtime era 4 apareceu 3 vezes.
        """

        full_column = df[column_label]

        count = 0
        is_counting = False
        instance_name = None
        dic = {}
        for i in range(0, len(full_column)):
            instances = 0
            if i > 0:
                if full_column[i] == full_column[i - 1]:
                    if not is_counting:
                        is_counting = True
                        instance_name = full_column[i]
                        count = 2
                    else:
                        count += 1
                else:
                    if is_counting:
                        is_counting = False
                        dic[str(instance_name)] = str(count)

        return dumps(dic)