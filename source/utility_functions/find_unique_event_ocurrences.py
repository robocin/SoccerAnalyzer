
def find_unique_event_ocurrences(dataframe, event):
    event_ocurrences_index = []
    for i in range(len(dataframe)):
        if(event in dataframe.iloc[i,1] and event not in dataframe.iloc[i-1,1] ):
             event_ocurrences_index.append(i)
        
        # if(dataframe.iloc[i,1] == event and dataframe.iloc[i-1,1] != event ):
        #     event_ocurrences_index.append(i)
    
    return event_ocurrences_index