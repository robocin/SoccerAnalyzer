def mean_of_lists(list_with_sublists):
    """
       Returns a list in which each index is the mean of the same index from all the other lists
       ---
       list must be a list containing one or more lists of int or floats. All sublists must have the same length.
       TODO: would be a good idea to check if all the sublists are of the same length as a safety measure? probably...
       """
    final_mean_list = []
    # for each index
    for i in range(0, len(list_with_sublists[0])):
        index_sum = 0
        # for each sublist
        for sub_list in list_with_sublists:
            # sum index_sum with the value of this list at that index i
            index_sum += sub_list[i][0]
        # after all lists values have been taken in consideration, take the mean
        index_mean = index_sum / len(list_with_sublists)
        # append the mean of this index to the final_mean_list
        final_mean_list.append(index_mean)

    return final_mean_list