from FeaturesLayouts import FoulsQuantity, FoulsProportion, Heatmaps, GoalReplay, PlayerReplay, StaminaTracker

# TODO: dentro de cada uma das funções chamadas abaixo, chamar clear_main_mdi_area.py para limpar todas as subWindows abertas no main mdiArea
#       (atualmente n estou fazendo isso pq está com um bug se ativar)

def show_feature(item_text, MainWindow, game_data):
    if(item_text == "Fouls Quantity"):
        FoulsQuantity.fouls_quantity(MainWindow, game_data)
    if(item_text == "Fouls Proportion"):
        FoulsProportion.fouls_proportion(MainWindow, game_data)
    if(item_text == "Heatmaps"):
        Heatmaps.heatmaps(MainWindow, game_data)
    if(item_text == "Goal Replay"):
        GoalReplay.goal_replay(MainWindow, game_data)
    if(item_text == "Player Replay"):
        PlayerReplay.player_replay(MainWindow, game_data)
    if(item_text == "Stamina Tracker"):
        StaminaTracker.stamina_tracker(MainWindow, game_data)


