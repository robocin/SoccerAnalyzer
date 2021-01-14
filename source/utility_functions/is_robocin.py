def is_robocin(team):
    team_l_name_to_lower = team.get_name().lower()

    if(team_l_name_to_lower=="robocin"):
        return True
    else:
        return False