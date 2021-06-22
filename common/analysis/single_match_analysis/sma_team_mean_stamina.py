import json

from AnalyzerBackend.utils.db_run_select_query import run_select_query
from AnalyzerCommon.common.operations.means import mean_of_lists


def sm_team_mean_stamina(match_object, team_side: str):
    """
    Returns a list containing two lists.
    ---
    """

    # get the stamina log of each player
    stamina_log_of_each_player = []
    for i in range(1, 12):
        aux = match_object.get_team(team_side).get_player(i).get_stamina_log()
        stamina_log_of_each_player.append(aux)

    team_mean_stamina = mean_of_lists(stamina_log_of_each_player)

    team_mean_stamina = json.dumps(team_mean_stamina)

    return team_mean_stamina
