
def find_unique_event_ocurrences(dataframe, event):
    event_ocurrences_index = []
    for i in range(1,len(dataframe)):
        if(event in dataframe.iloc[i,1] and event not in dataframe.iloc[i-1,1] and "kick" not in dataframe.iloc[i,1]):
             event_ocurrences_index.append(i+2)
             print(i+2)

    
    return event_ocurrences_index