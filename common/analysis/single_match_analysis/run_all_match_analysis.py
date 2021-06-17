from AnalyzerBackend.utils.db_run_alter_table_query import run_alter_table_query
from AnalyzerBackend.utils.db_run_insert_query import run_insert_query
from AnalyzerBackend.utils.db_run_select_query import run_select_query
from AnalyzerCommon.common.analysis.single_match_analysis.sma_team_mean_stamina import sm_team_mean_stamina


# TODO: I'm considering only 2D logs for now.
# def run_all_match_analysis(match_name, team_l_name, team_r_name, dataframe):
def run_all_match_analysis(match_object):
    """
    Compute all match analysis, insert all into a new entry in all_match_analysis
    entry.
    :return: python dict with the results of all analysis
    """

    # ADD ANALYSIS HERE
    # run all analysis and stores them in the analysis_value_tuple tuple
    #   each team mean stamina
    team_l_mean_stamina = sm_team_mean_stamina(match_object)
    team_r_mean_stamina = sm_team_mean_stamina(match_object)

    # ADD EACH COLUMN VALUE HERE
    # tuple containing the final values to be inserted each as a column in all_match_analysis
    analysis_values_tuple = (
        match_object.get_team("l").get_name(),
        match_object.get_team("r").get_name(),
        team_l_mean_stamina,
        team_r_mean_stamina
    )

    # ADD EACH COLUMN NAME HERE
    # tuple containing the name of each column to be inserted in all_match_analysis
    analysis_names_list = [
        'team_l_name',
        'team_r_name',
        'team_l_mean_stamina',
        'team_r_mean_stamina'
    ]

    analysis_dict = {}

    for i in range(0, len(analysis_names_list)):
        analysis_dict[str(analysis_names_list[i])] = analysis_values_tuple[i]

    return analysis_dict
