	#merging this one onto show_feature_events_position
	def show_feature_faults_position(self, mainWindowObject, feature_name, axes):
		data_to_plot = PlotData("scatter",2)
		
		teamL = data_to_plot.get_entry(0)
		teamL_x_positions = []
		teamL_y_positions = []

		teamR = data_to_plot.get_entry(1)
		teamR_x_positions = []
		teamR_y_positions = []
		
		for i in range(len(self.__data_frame)):
			if(self.__data_frame.iloc[i,1] == "foul_charge_l" and self.__data_frame.iloc[i-1,1] != "foul_charge_l"):
				teamL_x_positions.append(int(self.__data_frame.iloc[i,BALL_X]))
				teamL_y_positions.append(int(self.__data_frame.iloc[i,BALL_Y]))
			elif(self.__data_frame.iloc[i,1] == "foul_charge_r" and self.__data_frame.iloc[i-1,1] != "foul_charge_r"):
				teamR_x_positions.append(int(self.__data_frame.iloc[i,BALL_X]))
				teamR_y_positions.append(int(self.__data_frame.iloc[i,BALL_Y]))

		teamL.set_x_positions(teamL_x_positions)
		teamL.set_y_positions(teamL_y_positions)
		teamR.set_x_positions(teamR_x_positions)
		teamR.set_y_positions(teamR_y_positions)

		data_to_plot.get_entry(0).set_label(self.get_team_name("l"))
		data_to_plot.get_entry(1).set_label(self.get_team_name("r"))

		data_to_plot.set_background_image(plt.imread("files/soccerField.png"))
		data_to_plot.show_background_image()

		team_l_name_to_lower = data_to_plot.get_entry(0).get_label().lower()

		if(team_l_name_to_lower == "robocin"):
			data_to_plot.get_entry(0).set_color("#7da67d")
			data_to_plot.get_entry(1).set_color("#ffa1a1")
		else:
			data_to_plot.get_entry(0).set_color("#ffa1a1")
			data_to_plot.get_entry(1).set_color("#7da67d")

		self.plot_scattter(mainWindowObject, feature_name, data_to_plot, axes)
	#mergin this one onto show_feature_events_position
	def show_feature_goals_position(self, mainWindowObject, feature_name, axes):
		data_to_plot = PlotData("scatter",2)
		
		teamL = data_to_plot.get_entry(0)
		teamL_x_positions = []
		teamL_y_positions = []

		teamR = data_to_plot.get_entry(1)
		teamR_x_positions = []
		teamR_y_positions = []
		
		for i in range(len(self.__data_frame)):
			if(self.__data_frame.iloc[i,1] == "goal_l" and self.__data_frame.iloc[i-1,1] != "goal_l"):
				teamL_x_positions.append(int(self.__data_frame.iloc[i,10]))
				teamL_y_positions.append(int(self.__data_frame.iloc[i,11]))
			elif(self.__data_frame.iloc[i,1] == "goal_r" and self.__data_frame.iloc[i-1,1] != "goal_r"):
				teamR_x_positions.append(int(self.__data_frame.iloc[i,10]))
				teamR_y_positions.append(int(self.__data_frame.iloc[i,11]))

		teamL.set_x_positions(teamL_x_positions)
		teamL.set_y_positions(teamL_y_positions)
		teamR.set_x_positions(teamR_x_positions)
		teamR.set_y_positions(teamR_y_positions)

		data_to_plot.get_entry(0).set_label(self.get_team_name("l"))
		data_to_plot.get_entry(1).set_label(self.get_team_name("r"))

		data_to_plot.set_background_image(plt.imread("files/soccerField.png"))
		data_to_plot.show_background_image()

		team_l_name_to_lower = data_to_plot.get_entry(0).get_label().lower()
		team_r_name_to_lower = data_to_plot.get_entry(1).get_label().lower()

		if(team_l_name_to_lower == "robocin"):
			data_to_plot.get_entry(0).set_color("#7da67d")
			data_to_plot.get_entry(1).set_color("#ffa1a1")
		else:
			data_to_plot.get_entry(0).set_color("#ffa1a1")
			data_to_plot.get_entry(1).set_color("#7da67d")

		self.plot_graph(mainWindowObject, "scatter", title, data_to_plot, axes)