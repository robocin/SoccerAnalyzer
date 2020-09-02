from PyQt5.QtWidgets import QComboBox

def events_position_custom_layout(data, mainWindowObject):

    #### Definition of Functions ####
    # Response to event text changing
    def button_select_event_type_changed(currentText):
        # clear current plot_options layout
        clear_layout(mainWindowObject.plot_options)
        add_to_layout(button_select_event_type)

        # render custom layout
        if(currentText == "Goal"):
            add_to_layout(button_select_which_goal)
        if(currentText == "Foul"):
            add_to_layout(button_select_which_foul)
        if(currentText == "Penalty"):
            pass
        if(currentText == "Corner"):
            pass
    
    # Clear layout
    def clear_layout(layout):
        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().setParent(None)
   
    # Add a given widget to the plot_options layout
    def add_to_layout(widget):
        mainWindowObject.plot_options.addWidget(widget)

    #### Creating buttons layouts ####

    # Creates event selection combo box
    button_select_event_type = QComboBox()
    button_select_event_type.addItem("Goal")
    button_select_event_type.addItem("Foul")
    #button_select_event_type.addItem("Penalty")
    #button_select_event_type.addItem("Corner")
    
    # Creates: Goal > button to select which goal
    button_select_which_goal = QComboBox()
    for goal in data.get_all_events_object().get_all_goals():
        button_select_which_goal.addItem("Goal {} - Team {}".format(goal.get_chronological_id(), goal.get_who_scored().get_team_name()))
   
    # Creates: Fouls > button to select which foul
    button_select_which_foul = QComboBox()
    button_select_which_foul.addItem("Foul 1 time tal")
    button_select_which_foul.addItem("Foul 2 time tal")
    #for foul in data.get_all_events_object().get_all_fouls():
    #    foul_number_selection.addItem("Foul {} {}".format(foul.get_chronological_id(), foul.get_team()))

    
    #### Calling functions ####

    # At first,
    add_to_layout(button_select_event_type)
    add_to_layout(button_select_which_goal)

    # if a different event is selected, render the appropiate buttons
    button_select_event_type.currentTextChanged.connect(lambda: button_select_event_type_changed(button_select_event_type.currentText()))
    





'''
    comboBox_entity = QComboBox()
    comboBox_entity.addItem("ball")
    letters = "lr"
    for letter in letters:
        for i in range(1,12):
            comboBox_entity.addItem("player_" + letter + str(i))
    comboBox_entity.currentTextChanged.connect(lambda: self.comboBox_entity_chosen(comboBox_entity.currentText(), graph_type, axes))
'''
