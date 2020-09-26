import DataExtractor

def organize_data(file_path, game_data_var=None, game_statistics_var=None):
    if(game_data_var==None):
        # Call for data extraction
        game_data = DataExtractor.data_extractor(file_path)
    else:
        game_data = game_data_var
        DataExtractor.data_extractor(file_path, game_data)

    # Call for data computing
    #game_statistics = DataExtractor.data_computing(game_data)

    return (game_data)#,game_statistics)
