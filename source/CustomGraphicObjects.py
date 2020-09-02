from PyQt5.QtWidgets import QComboBox

def events_position_custom_layout(data, mainWindowObject):
    # Creates event selection combo box
    event_type_combo_box = QComboBox()
    event_type_combo_box.addItem("Goal")
    event_type_combo_box.addItem("Foul")
    event_type_combo_box.addItem("Penalty")
    event_type_combo_box.addItem("Corner")

    # if a different event is selected...
    event_type_combo_box.currentTextChanged.connect(lambda: event_type_combo_box_selected(event_type_combo_box.currentText()))
        # ...render the appropiate buttons/menus/comboBoxes
    def event_type_combo_box_selected(currentText):
        if(currentText == "Goal"):
            goal_number_selection = QComboBox()
            for goal in data.get_events().get_goals():
                goal_number_selection.addItem("Goal {}".format(goal.get_chronological_id()))
        if(currentText == "Foul"):
            foul_number_selection = QComboBox()
            for foul in data.get_events().get_fouls():
                foul_number_selection.addItem("Foul {} {}".format(foul.get_chronological_id(), foul.get_team()))
        if(currentText == "Penalty"):
            pass
        if(currentText == "Corner"):
            pass
    
    mainWindowObject.plot_options.addWidget(event_type_combo_box)





'''
    comboBox_entity = QComboBox()
    comboBox_entity.addItem("ball")
    letters = "lr"
    for letter in letters:
        for i in range(1,12):
            comboBox_entity.addItem("player_" + letter + str(i))
    comboBox_entity.currentTextChanged.connect(lambda: self.comboBox_entity_chosen(comboBox_entity.currentText(), graph_type, axes))
'''
