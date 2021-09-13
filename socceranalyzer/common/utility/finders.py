def find_first_unique_event_ocurrences(dataframe, event): # probably inefficient ? O(n)
    event_ocurrences_index = []
    for i in range(len(dataframe)):
        if(event in dataframe.iloc[i, 1] and event not in dataframe.iloc[i - 1, 1]):
            event_ocurrences_index.append(i)

    return event_ocurrences_index

def find_last_unique_event_ocurrences(dataframe, event): # probably inefficient ? O(n)
    event_ocurrences_index = []
    for i in range(len(dataframe)):
        if(event in dataframe.iloc[i, 1] and event not in dataframe.iloc[i - 1, 1]):
            while dataframe.iloc[i, 1] == event:
                i += 1
                if dataframe.iloc[i, 1] != event:
                    event_ocurrences_index.append(i)

    return event_ocurrences_index

def find_unique_event_count(dataframe, event): # not working
    event_ocurrences_index = []
    serie = dataframe[dataframe['playmode'] == event]
    
    for i in range(len(serie)):
        if(serie.iloc[i] != serie.iloc[i-1]):
            event_ocurrences_index.append(i)

    return event_ocurrences_index
