

def mean_list_given_multiple_lists(list):
    ''' Returns a list that in which each index is the mean of the same index from all the other lists '''
    # list must be a list containing one or more lists of int or floats. All sublists must have the same lenght. TODO: would be a good idea to check if all the sublists are of the same lenght as a safety measure?
    final_mean_list = []
    for i in range(0,len(list[0])): # for each index
        index_sum = 0 
        for sub_list in list: # for each sublist
            index_sum += sub_list[i]    # sum index_sum with the value of this list at that index i
        index_mean = index_sum / len(list) # after all lists values have been taken in consideration, take the mean
        final_mean_list.append(index_mean) # append the mean of this index to the final_mean_list
    return final_mean_list 