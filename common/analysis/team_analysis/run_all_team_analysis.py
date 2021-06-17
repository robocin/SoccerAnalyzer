from AnalyzerBackend.utils.db_run_alter_table_query import run_alter_table_query
from AnalyzerBackend.utils.db_run_insert_query import run_insert_query
from AnalyzerBackend.utils.db_run_select_query import run_select_query
from AnalyzerBackend.utils.db_run_update_table_query import run_update_table_query
from AnalyzerCommon.common.analysis.team_analysis.ta_team_mean_stamina import ta_team_mean_stamina
from AnalyzerCommon.common.entity.TeamOverview import TeamOverview


# todo: I'm considering only 2D logs for now
def run_all_team_analysis(team_object: TeamOverview):
    """
    Compute all team analysis, run an alter/insert query in its corresponding entry on all_team_analysis
    :param team_name: name of the team
    :return:         # team_r = match_object.get_team("r")
        # dataframe = make_query_for_single_team(cursor=cursor, team_side="r", team_name=team_l_name)
        # team_object = TeamOverview(dataframe, team_r_name)
        # analysis_dict = run_all_team_analysis(team_object)
        # update_te1
    """

    # ADD ANALYSIS HERE
    # run all analysis and stores them in the analysis_value_tuple tuple
    #   team mean stamina
    team_mean_stamina = ta_team_mean_stamina(team_object)

    # ADD EACH COLUMN VALUE HERE
    # tuple containing the final values to be inserted each as a column in all_match_analysis
    analysis_values_tuple = (
        team_mean_stamina,
    )

    # ADD EACH COLUMN NAME HERE
    # tuple containing the name of each column to be inserted in all_match_analysis
    analysis_names_list = [
        "team_mean_stamina"
    ]

    analysis_dict = {}

    for i in range(0, len(analysis_names_list)):
        analysis_dict[str(analysis_names_list[i])] = analysis_values_tuple[i]

    return analysis_dict

