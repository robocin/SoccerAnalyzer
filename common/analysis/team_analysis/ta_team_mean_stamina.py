import json
from AnalyzerCommon.common.entity.TeamOverview import TeamOverview
from AnalyzerCommon.common.operations.means import mean_of_lists


def ta_team_mean_stamina(team_object: TeamOverview):
    """
    Returns a list with the mean stamina of a team on all games
    :return: returns a list which is the mean stamina of the team across all matches
    """
    team_mean_stamina_for_each_match = team_object.get_mean_stamina_for_each_match()

    # if type(team_mean_stamina_for_each_match) == str:
    #     team_mean_stamina_for_each_match

    team_mean_stamina = mean_of_lists(team_mean_stamina_for_each_match)

    # team_mean_stamina = json.dumps(team_mean_stamina)

    return team_mean_stamina
