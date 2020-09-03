import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QComboBox

def events_position_custom_layout(data_collector, data, mainWindowObject, update_function, compute_and_set_x_and_y_positions):

    #### Definition of Functions ####
 
    # Clear layout
    def clear_layout(layout):
        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().setParent(None)
   
    # Add a given widget to the plot_options layout
    def add_to_layout(widget):
        mainWindowObject.plot_options.addWidget(widget)

    # Clear layout and then renders the default layout
    def reset_layout():
        clear_layout(mainWindowObject.plot_options)
        add_to_layout(button_event_type)

    # Response to event text changing
    def button_event_type_text_changed(currentText):
        reset_layout()

        # render custom layout
        if(currentText == "Goal"):
            plt.ion()
            add_to_layout(button_which_goal)
            compute_and_set_x_and_y_positions("goal", data)
            update_function(mainWindowObject.axes)
            plt.ioff()
        if(currentText == "Foul"):
            plt.ion() # TODO: (recorrente) precisa disso para atualizar o plot automaticamente, mas se clicar em outra feature e volta para a mesma, para de funcionar.... econtrar solução.
            add_to_layout(button_select_which_foul)
            compute_and_set_x_and_y_positions("foul_charge", data)
            update_function(mainWindowObject.axes)
            plt.ioff() # TODO: (recorrente) precisa disso para não bugar loucamente

        if(currentText == "Penalty"):
            pass
        if(currentText == "Corner"):
            pass
        
    def button_which_goal_text_changed(currentText, data_collector):
        if("Goal 1 -" in currentText):
            print("gol 1")
        elif("Goal 2 -" in currentText):
            print("gol 2")


    #### Creating buttons layouts ####

    # Creates event selection combo box
    button_event_type = QComboBox()
    button_event_type.addItem("Goal")
    button_event_type.addItem("Foul")
    #button_event_type.addItem("Penalty")
    #button_event_type.addItem("Corner")
    
    # Creates: Goal > button to select which goal
    button_which_goal = QComboBox()
    button_which_goal.addItem("All Goals")
    for goal in data_collector.get_all_events_object().get_all_goals():
        button_which_goal.addItem("Goal {} - Team {}".format(goal.get_chronological_id(), goal.get_who_scored().get_team_name()))
   
    # Creates: Fouls > button to select which foul
    button_select_which_foul = QComboBox()
    button_select_which_foul.addItem("All Fouls")
    button_select_which_foul.addItem("Foul 1 time tal")
    button_select_which_foul.addItem("Foul 2 time tal")
    #for foul in data_collector.get_all_events_object().get_all_fouls():
    #    foul_number_selection.addItem("Foul {} {}".format(foul.get_chronological_id(), foul.get_team()))

    
    #### Calling functions ####

    # Default layout
    add_to_layout(button_event_type)
    add_to_layout(button_which_goal)


    # Trigered events:

        # "button_event_type" (text changed) -> if a different event is selected, render the appropiate buttons
    button_event_type.currentTextChanged.connect(lambda: button_event_type_text_changed(button_event_type.currentText()))
        # "button_which_goal" (text changed) -> if a different goal is selected, render the corresponding plot
    button_which_goal.currentTextChanged.connect(lambda: button_which_goal_text_changed(button_which_goal.currentText(), data_collector))






'''
    comboBox_entity = QComboBox()
    comboBox_entity.addItem("ball")
    letters = "lr"
    for letter in letters:
        for i in range(1,12):
            comboBox_entity.addItem("player_" + letter + str(i))
    comboBox_entity.currentTextChanged.connect(lambda: self.comboBox_entity_chosen(comboBox_entity.currentText(), graph_type, axes))
'''
